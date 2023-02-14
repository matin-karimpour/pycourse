import numpy as np

a = np.array([1,2,4,6,86])
b = np.array([3,2,4,7,1])

comparison = a != b
print(comparison)
print(np.sum(comparison))