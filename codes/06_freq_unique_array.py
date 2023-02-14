import numpy as np

a = np.array([10, 15, 20, 10, 5, 1, 8, 7, 8])

uniq, freq = np.unique(a, return_counts=True)

print(uniq, "\n",freq)