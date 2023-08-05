# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumbpw']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'deal>=4.19.1,<5.0.0']

entry_points = \
{'console_scripts': ['dumbpw = dumbpw.cli:cli']}

setup_kwargs = {
    'name': 'dumbpw',
    'version': '0.3.0',
    'description': 'A bad password generator for bad websites with bad password policies',
    'long_description': 'dumbpw\n======================\n|LANGUAGE| |VERSION| |LICENSE| |MAINTAINED| |CIRCLECI| |MAINTAINABILITY|\n|STYLE|\n\n.. |CIRCLECI| image:: https://img.shields.io/circleci/build/gh/rpdelaney/dumbpw\n   :target: https://circleci.com/gh/rpdelaney/dumbpw/tree/main\n.. |LICENSE| image:: https://img.shields.io/badge/license-Apache%202.0-informational\n   :target: https://www.apache.org/licenses/LICENSE-2.0.txt\n.. |MAINTAINED| image:: https://img.shields.io/maintenance/yes/2022?logoColor=informational\n.. |VERSION| image:: https://img.shields.io/pypi/v/dumbpw\n   :target: https://pypi.org/project/dumbpw\n.. |STYLE| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n.. |LANGUAGE| image:: https://img.shields.io/pypi/pyversions/dumbpw\n.. |MAINTAINABILITY| image:: https://img.shields.io/codeclimate/maintainability-percentage/rpdelaney/dumbpw\n   :target: https://codeclimate.com/github/rpdelaney/dumbpw\n\nTo create and remember passwords for online services, the best practice for\nmost folks online is to use a password management tool such as `Bitwarden\n<https://bitwarden.com/>`_ to generate long, cryptographically random\npasswords. Then, a very strong passphrase is used to lock the password manager.\n\nUnfortunately, in a misguided attempt to encourage users to choose better\npasswords, many websites and apps have `very bad password policies <https://kottke.org/12/06/the-worlds-worst-password-requirements-list>`_\nthat place restrictions on what sorts of characters must be (or may not be) in\na password. These policies inhibit users from using cryptographically random\npassword generators. In fact, a long, high-entropy password is more likely to\nviolate such rules, which means a security-savvy user may have to attempt\nseveral "random" passwords before one is accepted.\n\nEnter dumbpw. dumbpw allows you to configure a set of rules, and then it will\ngenerate a cryptographically secure password that conforms to those dumb rules.\n\nIf all you need is a password generator, **you should not use this**.\n\nInstallation\n------------\n\n.. code-block :: console\n\n    pip3 install dumbpw\n\nUsage\n-----\n\n.. code-block :: console\n\n    $ dumbpw -h\n    Usage: dumbpw [OPTIONS]\n\n    Options:\n    --length INTEGER RANGE  The length of the password.  [1<=x<=512]\n    --uppercase INTEGER     The minimum number of uppercase characters.\n    --lowercase INTEGER     The minimum number of lowercase characters.\n    --digits INTEGER        The minimum number of digit characters.\n    --specials INTEGER      The minimum number of special characters.\n    --blocklist TEXT        Characters that may not be in the password.\n                            [default: \'";]\n    --help                  Show this message and exit.\n\ndumbpw uses `secrets <https://docs.python.org/3/library/secrets.html>`_\nto generate passwords.\n\n============\nDevelopment\n============\n\nTo install development dependencies, you will need `poetry <https://docs.pipenv.org/en/latest/>`_\nand `pre-commit <https://pre-commit.com/>`_.\n\n.. code-block :: console\n\n    pre-commit install --install-hooks\n    poetry install && poetry shell\n\n`direnv <https://direnv.net/>`_ is optional, but recommended for convenience.\n',
    'author': 'Ryan Delaney',
    'author_email': 'ryan.patrick.delaney@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/dumbpw',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
