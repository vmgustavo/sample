import os

from setuptools import setup, find_packages

install_requires = []
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'

if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='sample',
    version='0.1',
    author='Gustavo Maia',
    author_email='vm.gustavo31@gmail.com',
    long_description=long_description,
    long_description_content_type='',
    packages=find_packages(),
    install_requires=install_requires,
    description=''
)
