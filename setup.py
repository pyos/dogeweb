#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='dogeweb',
    version='HEAD',
    description='A functional web framework.',
    author='pyos',
    author_email='pyos100500@gmail.com',
    url='https://github.com/pyos/dogeweb',
    packages=['dogeweb'],
    package_dir={'dogeweb': 'dogeweb'},
    package_data={'dogeweb': ['*.dg']},
    install_requires=['aiohttp'],
)
