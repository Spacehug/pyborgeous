from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyborgeous',
    version='0.2.3',
    description='Pyborgeous',
    long_description=long_description,
    url='https://github.com/Spacehug/pyborgeous',
    author='Spacehug',
    author_email='spacehug.o0@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='jorge luis borges library unicode',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyborgeous=pyborgeous:main',
        ],
    },
)