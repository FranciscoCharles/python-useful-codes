import numpy as np


def normalize(array, max_value=1, array_type='float32'):
    diff = (array - array.min()).astype('float32')
    divider = diff.max()
    if divider == 0:
        divider = 1
    normalized_array = diff / divider
    return (max_value * normalized_array).astype(array_type)
