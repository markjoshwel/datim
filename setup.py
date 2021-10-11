# -*- coding: utf-8 -*-
# type: ignore

from setuptools import setup

modules = ["datim"]
install_requires = ["Pillow>=8.3.2,<9.0.0"]

extras_require = {"progress": ["tqdm>=4.62.3,<5.0.0"]}

entry_points = {"console_scripts": ["datim = datim:datim", "imdat = datim:imdat"]}

setup_kwargs = {
    "name": "datim",
    "version": "1.0.0",
    "description": "Data as an image.",
    "long_description": '# datim\n\nData as an image.\n\n## Installation\n\n```\npip install "git+https://github.com/markjoshwel/datim.git"\n```\n\n## Usage\n\ndatim has two commands, `datim` which converts data into images and `imdat`\nwhich converts converted data now represented as images back into the original\ndata.\n\n```shell\n$ datim\nusage: datim [-h] [-o] [-s] input output\n```\n\n```shell\n$ imdat\nimdat: datim [-h] [-o] [-s] input output\n```\n\n- `input`\n  input file path\n\n- `output`\n  output file path\n\n- `-h, --help`\n  Help message\n\n- `-o, --overwrite`\n  Overwrite without confirmation\n\n- `-s, --silent`\n  Do not use [tqdm](https://github.com/tqdm/tqdm) even if available\n\n## License\n\ndatim is unlicensed with [The Unlicense](https://unlicense.org).\n',
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
