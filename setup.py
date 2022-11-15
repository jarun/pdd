#!/usr/bin/env python3

import re
import os.path
import shutil
import sys

from setuptools import setup, find_packages

if os.path.isfile('pdd'):
    shutil.copyfile('pdd', 'pdd.py')

with open('pdd.py', encoding='utf-8') as f:
    version = re.search('_VERSION_ = \'([^\']+)\'', f.read()).group(1)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

tests_require=['pytest']

setup(
    name='pdd',
    version=version,
    description='Tiny date, time diff calculator with timers',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Arun Prakash Jana',
    author_email='engineerarun@gmail.com',
    url='https://github.com/jarun/pdd',
    license='GPLv3',
    python_requires='>=3.7',  # requires pip>=9.0.0
    platforms=['any'],
    py_modules=['pdd'],
    install_requires=['python-dateutil'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pdd=pdd:main']
    },
    extras_require={
        'tests': tests_require,
        'packaging': ['twine']
    },
    test_suite='test.py',
    tests_require=tests_require,
    keywords='date time calculator timer',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities'
    ]
)
