# Initializing Different Types of Array

import numpy as np
# All 0s matrix
zeros3d = np.zeros((2,3,3))
zeros2d = np.zeros((3,3))

# All 1s matrix
ones2d = ((2,2))

# Any other number
np.full((2,2), 33) # shape, val

# Any other number (full-like)
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print("Any other number (full-like) -> ", np.full_like(a , 4) )
print("\n")


# Random decimal numbers
np.random.rand(4,2,3)
np.random.random_sample(a.shape)

# Random integer values (4-7)
np.random.randint(4, 8, size = (3,3))

# The identity matrix
print("The identity matrix -> ", np.identity(3))
print("\n")

# Repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis = 0)
print("Repeat an array -> ", r1)
print("\n")

