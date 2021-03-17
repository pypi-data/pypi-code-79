import setuptools
import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(CUR_DIR, 'README.md')
with open('README.md', 'r', encoding='UTF-8') as fd:
    long_description = fd.read()

setuptools.setup(
    name='rainbond-python',
    version='1.0.19',
    description='Rainbond python cloud native development base library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/hekaiyou/rainbond-python",
    author="Kaiyou He",
    author_email="hky0313@outlook.com",
    packages=['rainbond_python'],
    include_package_data=True,
    install_requires=[
        'pymongo',
        'Flask',
        'pytest',
        'flask_cors',
        'redis',
        'websocket-client',
        'itsdangerous',
    ],
    keywords='rainbond python cloud native',
    entry_points={
        'console_scripts': [
            'rainbond = rainbond_python.cli:main'
        ],
    },
)
