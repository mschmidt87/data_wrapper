data_wrapper
========

A wrapper to conveniently store nested python dictionaries in nested directory structures using numpy binary files and yaml. It exposes two basic functions save() and load() to the user. 

![Python3.6](https://img.shields.io/badge/python-3.6-blue.svg)

# Example
    >>> import numpy as np
    >>> d = {'a1': np.arange(10.), 'a2': {'b2': 2}, 'a3': {'b3': np.arange(10.)}}
    >>> import data_wrapper.wrapper as dw
    >>> dw.save('example', d)

  Results in the following file structure:
  
    'example/a1.npy'
    'example/a2.yaml'
    'example/a3/b3.npy'
