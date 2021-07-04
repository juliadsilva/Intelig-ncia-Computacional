import os, sys
import numpy as np
from numpy import append, genfromtxt

class DataSets:

    @staticmethod
    def read(folder, filename):
        filename_abs = os.path.join(os.path.dirname(__file__), folder, filename)
        return genfromtxt(filename_abs, delimiter=",", dtype=float)

    @staticmethod
    def add_bias(arr, bias = -1):
        biased_arr = np.ndarray(shape=(arr.shape[0], arr.shape[1]+1), dtype=float)
        for i in range(0, len(arr)):
            biased_arr[i] = np.append(bias, arr[i])

        return biased_arr


class MOONS:
    input = DataSets.add_bias(DataSets.read("moons", "input.txt"))
    output = DataSets.read("moons", "output.txt")

