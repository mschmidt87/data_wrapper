# encoding: utf8
from setuptools import setup

setup(
<<<<<<< HEAD
    name='data_wrapper',
    version='0.0.1',
    author='Maximilian Schmidt',
    author_email='maximilian.schmidt@riken.jp',
    description=('Store nested python dictionaries in nested directory structures using binary numpy files and yaml.'),
    license='GPL2',
    keywords='numpy yaml',
    url='https://github.com/mschmidt87/data_wrapper',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*, !=3.4.*, <4',
    install_requires=['future'],
    packages=['data_wrapper'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
=======
    name='h5py_wrapper',
    version='1.1.0',
    author='Maximilian Schmidt, Jakob Jordan',
    author_email='max.schmidt@fz-juelich.de',
    description=('A wrapper to conveniently store nested Python dictionaries in hdf5 files.'),
    license='GPL2',
    keywords='hdf5 h5py',
    url='https://github.com/INM-6/h5py_wrapper',
    packages=['h5py_wrapper', 'tests'],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*, !=3.4.*, <4',
    scripts=['convert_h5file'],
    install_requires=['h5py', 'pytest-runner', 'future'],
    tests_require=['pytest'],
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
>>>>>>> f8b7009934fcce40407cc1d0225e92affb80ef91
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
