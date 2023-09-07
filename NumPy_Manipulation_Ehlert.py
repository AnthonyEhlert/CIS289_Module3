"""
Program Name: NumPy_Manipultation_Ehlert.py
Author: Tony Ehlert
Date: 9/7/2023

Program Description: This program creates a NumPy array and performs different manipulations on it and prints
the results to the console.
"""
import numpy as np

# create starting NumPy array
numpy_array = np.array([[1, 2, 5], [8, 0, -7], [7, 3, 9]])

# print the array to the console
print(numpy_array)

# transpose it and print to the console (overwrite original array)
numpy_array = numpy_array.transpose()
print(f"Print of transposed numpy_array:\n{numpy_array}")
print()

# swap axes and print to the console (Look familiar?) (overwrite original array)
numpy_array = np.swapaxes(numpy_array, 0, 1)
print(f"Print of numpy_array after swapping axes:\n{numpy_array}")
print()

# flip the array across horizontal axis (first row should be 5,2,1 after) & print to console (overwrite original array)
numpy_array = np.flip(numpy_array, axis=1)
print(f"Print of numpy_array after flipping across horizontal axis:\n{numpy_array}")
print()

# add a row to the bottom of array with values of 3,4,5 & print to console (overwrite original array)
numpy_array = np.append(numpy_array, [[3, 4, 5]], axis=0)
print(f"Print of numpy_array after adding row to bottom of array:\n{numpy_array}")
print()

# add a column to right of array with values 7,8,9,0 & print to console (overwrite original array)
numpy_array = np.insert(numpy_array, 3, [7,8,9,0], axis=1)
print(f"Print of numpy_array after adding column to right of array:\n{numpy_array}")
print()

"""
Array should now look like this
[[5  2  1  7]
 [-7 0  8  8]
 [9  3  7  9]
 [3  4  5  0]]
"""

# remove the last column in the array
numpy_array = np.delete(numpy_array, 3, axis=1)
#print(f"Print of numpy_array after deleting last column of array:\n{numpy_array}")
#print()

# reshape the array, so it is two columns & 6 rows & print to the console
numpy_array = np.reshape(numpy_array, (6,2))
print(f"Print of numpy_array after reshaping into 2 rows by 6 columns:\n{numpy_array}")
print()

# split the array into three 2x2 arrays and print the middle array
numpy_array = np.split(numpy_array, 3)
print(f"Print of numpy_array after splitting into three 2x2 arrays:\n{numpy_array}")
print()

# flatten the third array and print to console
numpy_array[2] = numpy_array[2].flatten()
print(f"Print of numpy_array after flattening the third array:\n{numpy_array}")
# for array in numpy_array:
#     print(array)

