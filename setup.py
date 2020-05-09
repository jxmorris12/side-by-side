from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='side-by-side',
    version='0.0.1',
    description='Print two files side-by-side (in columns)',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Jack Morris',
    author_email='jxmorris12@gmail.com',
    url='https://github.com/jxmorris12/side-by-side',
    license='MIT',
    packages=find_packages()
)