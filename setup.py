import setuptools
from setuptools import setup
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'r')
except(IOError, ImportError):
    long_description = open('README.md').read()


setuptools.setup(
    name='pystrategy_test_py',
    version="1.0.9",
    author = 'Francisco A. Prieto Rodriguez, Francisco de Asís Fernández Navarro, David Becerra Alonso',
    description = long_description,
    long_description_content_type= 'text/markdown',
    url = 'https://github.com/faprieto96/pystrategy_test_py',
    packages = setuptools.find_packages(),
    classifiers= [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)
