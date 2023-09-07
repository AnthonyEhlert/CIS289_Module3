"""
Program Name: NumPy_Math_Ehlert.py
Author: Tony Ehlert
Date: 9/7/2023

Program Description: This program creates two NumPy arrays and performs different math actions on them and prints
the results to the console.
"""
import numpy as np

# create two initial NumPy arrays
numpy_array_1 = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
numpy_array_2 = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

# print the first array to the console
print(f"Print of numpy_array_1:\n{numpy_array_1}")
print()

# print the first array's shape
print(f"Shape of numpy_array_1:\n{numpy_array_1.shape}")
print()

# print a 2x2 slice of the first array including the values from [0,0], to [1,1]
numpy_array_1_slice = numpy_array_1[0:2, 1:3]
print(f"Print of 2x2 slice of of numpy_array_1:\n{numpy_array_1_slice}")
print()

# output the boolean value of each element on whether the element is even (even = True, odd = False)
numpy_array_1_divide_by_2 = numpy_array_1 % 2 == 0
print(f"Print of boolean value for even numbers of numpy_array_1:\n{numpy_array_1_divide_by_2}")
print()

# using both arrays, print the output of adding the two arrays together elementwise
numpy_array_sum = np.add(numpy_array_1, numpy_array_2)
print(f"Print of sum of adding numpy_array_1 & numpy_array_2:\n{numpy_array_sum}")
print()

# using both arrays, print the output of multiplying the two arrays together elementwise
numpy_array_multiply = np.multiply(numpy_array_1, numpy_array_2)
print(f"Print of product of multiplying numpy_array_1 & numpy_array_2:\n{numpy_array_multiply}")
print()

# using the second array, print the sum of all elements in the array
numpy_array_2_sum = np.sum(numpy_array_2)
print(f"Print of sum of all elements in numpy_array_2:\n{numpy_array_2_sum}")
print()

# using the second array, print the product of all the elements in the array
numpy_array_2_product = np.prod(numpy_array_2)
print(f"Print of product of all elements in numpy_array_2:\n{numpy_array_2_product}")
print()

# using the second array, print the maximum and minimum value of the elements in the array
numpy_array_2_max = np.max(numpy_array_2)
numpy_array_2_min = np.min(numpy_array_2)
print(f"Print of max element in numpy_array_2:\n{numpy_array_2_max}")
print()
print(f"Print of min element in numpy_array_2:\n{numpy_array_2_min}")