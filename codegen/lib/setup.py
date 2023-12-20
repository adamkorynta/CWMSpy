# coding: utf-8

"""
    CWMS Data API

    CWMS REST API for Data Retrieval  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "CWMSpy"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="CWMS Data API",
    author_email="",
    url=" https://github.com/Enovotny/CWMSpy",
    keywords=["Swagger", "CWMS Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    CWMS REST API for Data Retrieval  # noqa: E501
    """
)
