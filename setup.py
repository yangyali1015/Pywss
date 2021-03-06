import os
import re
import codecs

from setuptools import setup, find_packages

"""pip install twine
1、python setup check
2、python setup sdist
3、twine upload dist/__packages__-__version__.tar.gz
"""


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r', encoding='utf-8').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name='pywss',
    version=find_version('pywss', 'version.py'),
    description="This is a web-socket-server by python",
    long_description="see https://github.com/CzaOrz/Pywss",
    author='czaOrz',
    author_email='972542644@qq.com',
    url='https://github.com/CzaOrz/Pywss',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        "logor >= 0.0.4"
    ],
)
