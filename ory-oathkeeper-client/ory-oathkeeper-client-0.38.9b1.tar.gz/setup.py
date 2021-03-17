"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.38.9-beta.1
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ory-oathkeeper-client"
VERSION = "v0.38.9-beta.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="ORY Oathkeeper",
    author="ORY",
    author_email="hi@ory.am",
    url="https://github.com/ory/sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "ORY Oathkeeper"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501
    """
)
