from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyborgeous',
    version='0.5.1',
    description='Pyborgeous is an implementation of Jorge Luis Borges\' Library of Babel',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6.1',
    ],
    keywords='Jorge Luis Borges Library of Babel unicode',
    packages=find_packages(),
    install_requires=['markovify'],
    include_package_data=True,
    zip_safe=True,
    entry_points={'console_scripts': ['pyborgeous=pyborgeous:main']},
)