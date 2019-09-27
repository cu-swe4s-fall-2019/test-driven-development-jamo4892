import sys
import math_lib
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def boxplot(L, out_file_name):
    """
    Purpose
    -------
    This function makes a box plot of an input array of numbers
    and saves the plot to a file.

    Inputs
    ------
    L: Integer array
    Array of column values from standardin

    out_file_name: string
    File name fo saving the plot

    Outputs
    -------
    A file of the plot is saved to the input file name.
    """

    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    # Find mean and standard deviation of L using math_lib.py.


def histogram(L, out_file_name):
    """
    Purpose
    -------
    This function makes a histogram plot of an input array of numbers
    and saves the plot to a file.

    Inputs
    ------
    L: Integer array
    Array of column values from standardin

    out_file_name: string
    File name fo saving the plot

    Outputs
    -------
    A file of the plot is saved to the input file name.
    """

    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    # Find mean and standard deviation of L using math_lib.py.


def combo(L, out_file_name):
    """
    Purpose
    -------
    This function makes a combination plot of a box plot and
    a histogram plot of an input array of numbers
    and saves the plot to a file.

    Inputs
    ------
    L: Integer array
    Array of column values from standardin

    out_file_name: string
    File name fo saving the plot

    Outputs
    -------
    A file of the plot is saved to the input file name.
    """

    mean = math_lib.list_mean(L)
    stdev = math_lib.list_stdev(L)
    # Find mean and standard deviation of L using math_lib.py.
