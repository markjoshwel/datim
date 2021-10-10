# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['datim']
install_requires = \
['Pillow>=8.3.2,<9.0.0']

extras_require = \
{'progress': ['tqdm>=4.62.3,<5.0.0']}

entry_points = \
{'console_scripts': ['datim = datim:datim', 'imdat = datim:imdat']}

setup_kwargs = {
    'name': 'datim',
    'version': '1.0.0',
    'description': 'Data as an image.',
    'long_description': '# datim\n\nData as an image.\n\n## Installation\n\n```\npip install ""\n```\n\n## Usgae\n\n## License\n\ndatim is unlicensed with [The Unlicense](https://unlicense.org).\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/markjoshwel/datim',
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)

