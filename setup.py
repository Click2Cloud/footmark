#!/usr/bin/env python
# Always prefer setuptools over distutils
from codecs import open
from os import path

try:
    from setuptools import setup

    extra = dict(test_suite="tests.test.suite", include_package_data=True)
except ImportError:
    from distutils.core import setup

    extra = {}

PACKAGE = "footmark"
NAME = "footmark"
DESCRIPTION = "A Python interface to Aliyun Web Services"
AUTHOR = "xiaozhu"
AUTHOR_EMAIL = "heguimin36@163.com"
URL = ""
VERSION = __import__(PACKAGE).__version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=VERSION,

    description=DESCRIPTION,
    long_description=long_description,

    # The project's main homepage.
    url=URL,

    # Author details
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["footmark", "footmark.ecs", "footmark.slb", "footmark.vpc", "footmark.rds", "footmark.oss", "footmark.pyami"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['aliyun-python-sdk-ecs>=2.1.0', 'aliyun-python-sdk-slb>=2.0.21', 'aliyun-python-sdk-core>=2.3.2',
                      'aliyun-python-sdk-rds>=2.1.0', 'oss2>=2.3.3', 'importlib']
)
