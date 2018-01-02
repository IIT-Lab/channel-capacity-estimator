"""Data engineering functions, as adding some dust or normalisation"""
import numpy as np


def _project_labels(data):
    return [x[0] for x in data]


def _project_coords(data):
    return [x[1] for x in data]


def normalise(data):
    """Data normalisation

    Parameters
    ----------
    data : list
        data is a list of tuples. Each tuples has form (label, value), where label can be either int or string
        and value is a one-dimensional numpy array/list representing coordinates

    Returns
    -------
    list
        list of data points. Each data point is normalised, what means that each coordinate is in the interval
        [0, 1]
    """
    lab = _project_labels(data)
    arr = _project_coords(data)
    arr = np.array(arr)

    b = np.amax(arr)
    a = np.amin(arr)

    arr = (arr-a) / (b-a)

    return list(zip(lab, arr))
