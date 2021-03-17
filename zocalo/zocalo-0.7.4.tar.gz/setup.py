#!/usr/bin/env python

from setuptools import setup, find_packages

_rst_section = "\n--------"

with open("README.rst") as readme_file:
    readme = readme_file.read()

    # Only take text up to the first section
    if _rst_section in readme:
        readme = readme.split(_rst_section)[0]
        readme = "\n".join(readme.split("\n")[:-1])

with open("HISTORY.rst") as history_file:
    history = history_file.read()

    # Only take text from up to 6 sections
    _history_split = history.split(_rst_section)
    if len(_history_split) > 7:
        history = _rst_section.join(_history_split[:7])
        history = "\n".join(history.split("\n")[:-1])

requirements = ["graypy", "setuptools", "workflows"]
setup_requirements = []
test_requirements = ["pytest"]

setup(
    author="Markus Gerstel",
    author_email="scientificsoftware@diamond.ac.uk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Infrastructure components for automated data processing at Diamond Light Source",
    entry_points={
        "console_scripts": [
            "zocalo.go = zocalo.cli.go:run",
            "zocalo.service = zocalo.service:start_service",
            "zocalo.wrap = zocalo.cli.wrap:run",
        ],
        "libtbx.dispatcher.script": [
            "zocalo.go = zocalo.go",
            "zocalo.service = zocalo.service",
            "zocalo.wrap = zocalo.wrap",
        ],
        "libtbx.precommit": ["zocalo = zocalo"],
        "workflows.services": [
            "Schlockmeister = zocalo.service.schlockmeister:Schlockmeister"
        ],
        "zocalo.wrappers": ["dummy = zocalo.wrapper:DummyWrapper"],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="zocalo",
    name="zocalo",
    packages=find_packages(),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/DiamondLightSource/zocalo-python",
    version="0.7.4",
    zip_safe=False,
)
