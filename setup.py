import setuptools
from setuptools import setup, find_packages

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# this grabs the requirements from requirements.txt
required_libs = {}
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines() if i.split("==")[0] in required_libs]


setup(
    name='oneid_metadata',
    version='0.0.1',
    include_package_data=True,
    package_data={
        "": ["*.json"],
    },
    install_requires=[
        REQUIREMENTS
    ],
    packages=find_packages(
        where='src'
    ),
    package_dir={"": "src"}
)

