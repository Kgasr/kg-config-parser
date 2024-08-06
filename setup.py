# setup.py

from setuptools import setup, find_packages

setup(
    name='kg-config-parser',
    version='0.0.1',
    description='A toolkit for reading various file formats like YAML and JSON.',
    url='https://github.com/Kgasr/kg-config-parser',
    author='Karan Gupta',
    author_email='karangupta125@gmail.com',
    packages=find_packages(),
    install_requires=['PyYAML'],
)
