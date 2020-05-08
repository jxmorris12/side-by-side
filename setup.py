from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='side-by-side',
    version='0.0.1',
    description='Print two files side-by-side (in columns)',
    long_description=readme,
    author='Jack Morris',
    author_email='jxmorris12@gmail.com',
    url='https://github.com/jxmorris12/side-by-side',
    license=license,
    packages=find_packages()
)