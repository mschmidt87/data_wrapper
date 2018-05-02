import numpy as np
import os
import yaml


def save(directory, dic, prefix=''):
    """
    Save a Python dictionary to a given directory.
    The function stored all numpy arrays in the dictionary to numpy
    binary files and tries to store scalar data to yaml files.

    Parameters
    ----------
    directory : str
        Path to the top directory where the data is stored.
    dic : dict
        Dictionary to be stored.
    prefix : str
        Prefix that is preprended to the names of the dictionary keys
        to form the filename.
        Defaults to an empty string.
    Examples
    --------
    >>> import numpy as np
    >>> d = {'a1': np.arange(10.), 'a2': {'b2': 2}, 'a3': {'b3': np.arange(10.)}}
    >>> import dict_wrapper.wrapper as dw
    >>> dw.save('example', d)

    results in the following file structure:
    'example/a1.npy'
    'example/a2.yaml'
    'example/a3/b3.npy'
    """
    if not os.path.isdir(directory):
        os.mkdir(directory)
    for key, val in dic.items():
        fn = os.path.join(directory, '{}{}'.format(prefix, key))
        if isinstance(val, np.ndarray):
            np.save(fn, val)
        elif isinstance(val, dict):
            if not np.any(list(map(lambda x: isinstance(x, np.ndarray), val.values()))):
                fn = os.path.join(directory, '{}.yaml'.format(key))
                with open(fn, 'w') as f:
                    yaml.dump(val, f)
            else:
                save(fn, val)
    

def load(directory, prefix=''):
    """
    Load data from a given directory into a Python dictionary.

    Parameters
    ----------
    directory : str
        Path to the top directory where the data is stored
    prefix : str
        Prefix of the filenames that will be ignored to for the names
        of the keys in the returnedPython dictionary.
    """
    files = os.listdir(directory)
    d = {}
    for fn in files:
        key = os.path.splitext(fn)[0].split('_')[-1]
        try:
            data = np.load(fn)
            d[key] = data
        except OSError:
            import pdb; pdb.set_trace()
            try:
                with open(fn, 'r') as f:
                    data = yaml.load(f)
                d[key] = data
            except:
                pass
    return d
