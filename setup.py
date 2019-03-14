from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-pip-package-starter-kit',
    version='0.0.1',
    description='Sample package from Schubert',
    long_description=readme,
    author='Raphael Schubert',
    author_email='rfswdp@gmail.com',
    url='https://github.com/rfschubert/python-pip-package-starter-kit',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)