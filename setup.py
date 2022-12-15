import setuptools
from setuptools import setup, find_packages

setup(
    name='spark_transformer',
    version='0.0.1',
    include_package_data=True,
    package_data={
        "": ["*.json"],
    },
    install_requires=[
        "jsonpickle"
    ],
    packages=find_packages(
        where='src'
    ),
    package_dir={"": "src"}
)

