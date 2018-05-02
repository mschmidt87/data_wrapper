# encoding: utf8

"""
dict_wrapper
============

Wrapper to conveniently store arbitrarily nested python dictionaries
to nested dictory structures using numpy binary data files and yaml.

Functions
---------

- save : store nested dictionary in a given directory 
- load : load nested dictionary from a given directory

"""

from .wrapper import save
from .wrapper import load


__version__ = '0.0.1'
