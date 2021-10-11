# -*- coding: utf-8 -*-
# type: ignore
from setuptools import setup

modules = ["datim"]
install_requires = ["Pillow>=8.3.2,<9.0.0", "lz4>=3.1.3,<4.0.0"]

extras_require = {"optional": ["tqdm>=4.62.3,<5.0.0"]}

entry_points = {
    "console_scripts": ["datim = datim:setup_datim", "imdat = datim:setup_imdat"]
}

setup_kwargs = {
    "name": "datim",
    "version": "1.1.0",
    "description": "Data as an image.",
    "long_description": '# datim\n\nData as an image.\n\n- [Installation](#installation)\n\n- [Usage](#usage)\n\n- [Optional Features](#optional-features)\n\n- [Details](#details)\n\n- [Potential Improvement](#potential-improvement)\n\n- [License](#license)\n\n## Installation\n\n```\npip install "git+https://github.com/markjoshwel/datim.git"\n```\n\nFor [optional features](#optional-features), use this instead:\n\n```\npip install "datim[optional] @ git+https://github.com/markjoshwel/datim.git"\n```\n\n## Usage\n\ndatim has two commands, `datim` which converts data into images and `imdat`\nwhich converts converted data now represented as images back into the original\ndata.\n\n```\n$ datim\nusage: datim [-h] [-o] [-s] [-nc] input output\n\nturns any file into an image\n\npositional arguments:\n  input               input file path\n  output              output file path\n\noptional arguments:\n  -h, --help          show this help message and exit\n  -o, --overwrite     overwrite without confirmation\n  -s, --silent        do not use tqdm even if available\n  -nc, --no-compress  do not compress data using zlib\n```\n\n```\n$ imdat\nusage: imdat [-h] [-o] [-s] [-nc] input output\n\nturns previously converted images into the original file\n\npositional arguments:\n  input               input file path\n  output              output file path\n\noptional arguments:\n  -h, --help          show this help message and exit\n  -o, --overwrite     overwrite without confirmation\n  -s, --silent        do not use tqdm even if available\n  -nc, --no-compress  do not compress data using zlib\n```\n\n## Optional Features\n\n- **[tqdm](https://github.com/tqdm/tqdm) Support**\n\n  If `tqdm` is installed, a progress bar is shown during image generation\n  (`datim`) and image reversal (`imdat`).\n\n## Details\n\nAn image created by datim is made up by the following:\n`[header][data][trailing random data]`\n\n- `[header]`\n\n  This is made up of a base15 hex array (0-E) denoting the length of the\n  (compressed) data hex array. It is then suffixed with a hex `F`, acting as a\n  delimiter betweeen the `[header]` and `[data]` sections. This method of\n  storing the data hex array was chosen as to not use the alpha layer, which\n  would increase the resulting image file size.\n\n- `[data]`\n\n  The (compressed) data is expressed naturally as its hexidecimal counterparts.\n\n- `[trailing random data]`\n\n  After the `[data]` hex array, there are trailing randomly generated hex\n  chars. This is done purely for cosmetics.\n\n## Potential Improvement  \n\n- **Efficient Sizing**\n\n  There may be a way to figure the smallest possible width and height values\n  from the total length of the (compressed) hex array rather than ceiling the\n  length and square rooting it, which may help reduce size.\n\n## License\n\ndatim is unlicensed with [The Unlicense](https://unlicense.org).\n',
    "author": "Your Name",
    "author_email": "you@example.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/markjoshwel/datim",
    "py_modules": modules,
    "install_requires": install_requires,
    "extras_require": extras_require,
    "entry_points": entry_points,
    "python_requires": ">=3.6.2,<4.0.0",
}


setup(**setup_kwargs)
