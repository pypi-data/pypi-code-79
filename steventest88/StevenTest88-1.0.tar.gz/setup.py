import setuptools
from pathlib import Path

setuptools.setup(
    name="StevenTest88",
    version=1.0,
    long_description=Path("README").read_text(),
    packages=setuptools.find_packages()
)
