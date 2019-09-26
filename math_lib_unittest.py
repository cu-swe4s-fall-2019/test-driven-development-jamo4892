"""This script contains unit tests for math_lib.py. It is run by a call
from the .travis.yml file in this code repository."""

import unittest
import sys
import os
import math_lib
import random
import statistics
# Import modules.


class Test_Math_Lib(unittest.TestCase):

    def test_list_mean_empty(self):
        e = math_lib.list_mean(None)
        self.assertEqual(e, None)
        # Check that a 'None' entry to math_lib.list_mean returns 'None'

    def test_list_mean_ones(self):
        a = math_lib.list_mean([1, 1, 1, 1, 1])
        self.assertEqual(a, 1)
        # Check that an array of 1s has an average of 1

    def test_list_mean_randint(self):
        R = []
        for i in range(100):
            R.append(random.randint(0, 100))
        avg_listmean = math_lib.list_mean(R)
        avg_stat = statistics.mean(R)
        self.assertEqual(round(avg_listmean, 4), round(avg_stat, 4))
        # Check that an array of random integers passed to list_mean returns
        # the same value as the mean calculated by Python

    def test_list_mean_randfloat(self):
        F = []
        for i in range(100):
            F.append(random.uniform(-200, 300))
        avg_listmean = math_lib.list_mean(F)
        avg_stat = statistics.mean(F)
        self.assertEqual(round(avg_listmean, 4), round(avg_stat, 4))
        # Check that an array of random floats passed to list_mean returns
        # the same value as the mean calculated by Python

    def test_list_stdev_empty(self):
        e = math_lib.list_stdev(None)
        self.assertEqual(e, None)
        # Check that a 'None' entry to math_lib.list_stdev returns 'None'

    def test_list_stdev_ones(self):
        s = math_lib.list_stdev([1, 1, 1, 1, 1])
        self.assertEqual(s, 0)
        # Check that an array of 1s has a standard deviation of 0

    def test_list_stdev_randint(self):
        R = []
        for i in range(100):
            R.append(random.randint(0, 100))
        stdev_liststdev = math_lib.list_stdev(R)
        stdev_stat = statistics.pstdev(R)
        self.assertEqual(round(stdev_liststdev, 4), round(stdev_stat, 4))
        # Check that an array of random integers passed to list_stdev returns
        # the same value as the standard deviation calculated by Python

    def test_list_stdev_randfloat(self):
        F = []
        for i in range(100):
            F.append(random.uniform(-500, 1000))
        stdev_liststdev = math_lib.list_stdev(F)
        stdev_stat = statistics.pstdev(F)
        self.assertEqual(round(stdev_liststdev, 4), round(stdev_stat, 4))
        # Check that an array of random floats passed to list_stdev returns
        # the same value as the standard deviation calculated by Python


if __name__ == '__main__':
    unittest.main()
