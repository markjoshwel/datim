# type: ignore

from setuptools import setup

modules = ["datim"]
install_requires = ["Pillow>=8.3.2,<9.0.0", "lz4>=3.1.3,<4.0.0"]

extras_require = {"optional": ["tqdm>=4.62.3,<5.0.0"]}

entry_points = {
    "console_scripts": [
        "datim = datim:setupc_datim",
        "datimp = datim:setup_datim",
        "imdat = datim:setupc_imdat",
        "imdatp = datim:setup_imdat",
    ]
}

setup_kwargs = {
    "name": "datim",
    "version": "2.0.2",
    "description": "Data as an image.",
    "long_description": '# datim 2.0.2\n\nData as an image.\n\n- [Installation](#installation)\n- [Usage](#usage)\n- [Changelog](CHANGELOG.md)\n- [Details](#details)\n- [License](#license)\n\n## Installation\n\n```\npip install datim\n```\n\nAlternatively, install `datim[optional]` and get progress bar support.\n\n## Usage\n\ndatim has four commands:\n\n\n- `datim`\n- `imdat`\n- `datimp`\n- `imdatp`\n\n`datim` and `imdat` check whether the compiled variant of datim is installed.\nIf unavailable, it will fallback to the pure Python variant of datim.\n`datimp` and `imdatp` _exclusively_ use the pure Python variant of the module.\n\n```\n$ datim\nusage: datim [-h] [-o] [-np] [-nc] [-na] input output\n\n(compiled) turns any file into an image\n\npositional arguments:\n  input               input file path\n  output              output file path\n\noptional arguments:\n  -h, --help          show this help message and exit\n  -o, --overwrite     overwrite without confirmation\n  -np, --no-progress  do not use tqdm\n  -nc, --no-compress  do not compress data\n  -na, --no-alpha     do not use alpha channel\n```\n\n```\n$ imdat\nusage: imdat [-h] [-o] [-np] [-nc] [-na] input output\n\n(compiled) turns previously converted images into the original file\n\npositional arguments:\n  input               input file path\n  output              output file path\n\noptional arguments:\n  -h, --help          show this help message and exit\n  -o, --overwrite     overwrite without confirmation\n  -np, --no-progress  do not use tqdm\n  -nc, --no-compress  do not compress data\n  -na, --no-alpha     do not use alpha channel\n```\n\n## Details\n\nAn image created by datim is made up by the following:\n`[header][data][trailing random data]`\n\n- `[header] -> "<length of [data] hex array encoded in base15 hex>F"`\n\n  This is made up of a base15 hex array (0-E) denoting the length of the\n  (compressed) data hex array. It is then suffixed with a hex `F`, acting as a\n  delimiter betweeen the `[header]` and `[data]` section. This method of\n  storing the data hex array was chosen as to not use the alpha layer, which\n  would increase the resulting image file size.\n\n- `[data]`\n\n  The (compressed) data is expressed naturally as its hexidecimal counterparts.\n\n- `[trailing 0s]`\n\n  After the `[data]` hex array are trailing `0`s. Before 2.0.0, trailing data\n  were randomly generated for cosmetic purposes, but was removed due for\n  performance.\n\n## License\n\ndatim is unlicensed with [The Unlicense](https://unlicense.org).\n',
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

from build import *

if build(setup_kwargs):
    try:
        setup(**setup_kwargs)

    except Exception as e:
        print(
            "Something went wrong during installation, attempting a non-compiled install."
        )

        del setup_kwargs["ext_modules"]

        setup(**setup_kwargs)

else:
    setup(**setup_kwargs)
