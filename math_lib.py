"""
Purpose
-------
This script takes a numerical array as input and returns either the mean
or the standard deviation of the array.

Inputs
------
L: Integer list
List of integer values

Outputs
-------
Mean: mean of the input list

Stdev: standard deviation of the input list
"""

import math
# Import modules


def list_mean(L):
    if L is None:
        return None

    if len(L) == 0:
        return None

    s = 0
    for l in L:
        try:
            s += l
        except ValueError:
            raiseValueError('Unsupported value in list')
            sys.exit(1)

    return s / len(L)
    sys.exit(0)
    # Find the mean of the array


def list_stdev(L):
    if L is None:
        return None

    if len(L) == 0:
        return None

    s = 0
    for l in L:
        try:
            s += l
        except ValueError:
            raiseValueError('Unsupported value in list')
            sys.exit(1)

    avg = list_mean(L)
    return math.sqrt(sum([(avg-x)**2 for x in L]) / len(L))
    sys.exit(0)
    # Find the standard deviation of the array
