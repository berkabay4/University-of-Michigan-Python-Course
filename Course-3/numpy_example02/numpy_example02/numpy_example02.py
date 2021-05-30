# Accessing/Changig specific elements, row, columns etc.

import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print("Matris A ->", a)

# Get a specific element [r,c]
print("2. row, 6. column ->", a[1,5]) # or a[1, -2]

# Get a specific row
print("1. Row -> ", a[0, :])

# Get a specific column
print("3. Column -> ", a[:, 4])

# [startindex:endindex:stepsize]
print("Example -> ", a[0, 1:6:2])

# Change value in A Matris
print('\n')
print('Before A Matris -> ', a )
print('\n')

a[1,5] = 20
print('After A Matris -> ', a)
print('\n')

#All row
a[:, 2] = [45, 46]
print("Change all row in 2. row ->",  a)
print('\n')

# All column
a[0, :] = 0
print("Change all column in 1. column ->",  a)
print('\n')

# 3D Example 
x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("X Matris -> ", x)
print('\n')

print("X Dimension = ", x.ndim)

# Get specific element (work outside in)
x[1,0,1] = 12
print("New X Matris", x)