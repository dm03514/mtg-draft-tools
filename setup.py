import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name = "mtgdrafttools",
    version = "0.1dev",
    packages = find_packages(),
)

