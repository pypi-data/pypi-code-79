#!/usr/bin/env python
import sys

from setuptools import setup, find_packages
import cfc
import os


def path_in_project(*path):
    return os.path.join(os.path.dirname(__file__), *path)


def read_file(filename):
    with open(path_in_project(filename)) as f:
        return f.read()


def read_requirements(filename):
    contents = read_file(filename).strip('\n')
    return contents.split('\n') if contents else []


if sys.version_info[:3] < (3, 6, 1):
    raise Exception("Coffin Codes requires Python >= 3.6.1.")

description = 'Get your localhost online and https - Ngrok Alternative'
setup(
    name='cfc-bsb',
    version=cfc.__version__,
    description=description,
    long_description=description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='Coffin Codes live localhost online https ngrok alternative',
    author='Coffin Codes V4',
    author_email='sphabsb2192@gmail.com',
    maintainer='BSB Developers',
    maintainer_email='sphabsb2192@gmail.com',
    url='https://github.com/Sphabsb2192/codes',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cfc = cfc.main:main',
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    python_requires='>=3.6.1',
)
