# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['inmanta_dev_dependencies']

package_data = \
{'': ['*']}

install_requires = \
['black==22.1.0',
 'flake8-black==0.3.2',
 'flake8-copyright==0.2.2',
 'flake8-isort==4.1.1',
 'flake8==3.9.2',
 'isort==5.10.1',
 'lxml==4.8.0',
 'mypy==0.942',
 'pep8-naming==0.12.1',
 'pytest==7.1.1']

extras_require = \
{'async': ['pytest-asyncio==0.18.2', 'pytest-timeout==2.1.0'],
 'core': ['pytest-env==0.6.2',
          'pytest-postgresql==4.1.1',
          'tox==3.24.5',
          'asyncpg>=0.21.0,<1.0.0',
          'tornado>=6.1,<7.0'],
 'extension': ['pytest-inmanta-extensions',
               'pytest-env==0.6.2',
               'pytest-postgresql==4.1.1',
               'tox==3.24.5',
               'asyncpg>=0.21.0,<1.0.0',
               'tornado>=6.1,<7.0'],
 'module': ['pytest-inmanta'],
 'pytest': ['pytest-env==0.6.2',
            'pytest-cover==3.0.0',
            'pytest-randomly==3.11.0',
            'pytest-xdist==2.5.0',
            'pytest-sugar==0.9.4',
            'pytest-sugar==0.9.4',
            'pytest-instafail==0.4.2',
            'pytest-instafail==0.4.2'],
 'sphinx': ['inmanta-sphinx==1.5.0',
            'sphinx-argparse==0.3.1',
            'sphinx-autodoc-annotation==1.0-1',
            'sphinx-rtd-theme==1.0.0',
            'sphinx-tabs==3.3.1',
            'Sphinx==4.4.0',
            'sphinxcontrib-serializinghtml==1.1.5',
            'sphinxcontrib-redoc==1.6.0',
            'sphinx-click==3.1.0',
            'recommonmark==0.7.1']}

setup_kwargs = {
    'name': 'inmanta-dev-dependencies',
    'version': '2.11.0',
    'description': 'Package collecting all common dev dependencies of inmanta modules and extensions to synchronize dependency versions.',
    'long_description': None,
    'author': 'Inmanta',
    'author_email': 'code@inmanta.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
