import numpy as np 

arr1 = np.eye(3)
print("original array:\n",arr1)

arr_with_pad = np.pad(
        array=arr1,
        pad_width=2,
        mode='constant',
        constant_values=8,)
print("\n array with padding:\n",arr_with_pad)

