# import numpy as np


# na = np.array([])

# nb = np.array([1, 'qwe', 123])

# print(nb)

import multiprocessing as mp
print("Number of processors: ", mp.cpu_count())

import dill
print(dill.license())