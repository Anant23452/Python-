import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print("\n")

# 2d Array
arr_2d =np.array([[1,2,3,4,5,],[9,8,7,5,4,]])
print(arr_2d)
print(arr_2d.shape)  # Shape of the array
print(arr_2d.dtype)  # Data type of the array

# 3d Array
arr_3d = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(arr_3d)
mean = np.mean(arr_3d)  # Mean of the array
print(f"mean of array {mean}")