# Mathematics
import numpy as np

a = np.array([1,2,3,4])
print('Matrix A -> ', a)
print('\n')

# Add/Sub/Mul/Div all element
a = a + 2
print('A+2 -> ', a)
print('\n')

a = a - 2 
a = a * 2
a = a / 2

# Take the sin/cos
np.cos(a)

# Linear Algebra
a = np.ones((2,3))
print('New A Matrix -> ', a)
print('\n')

b = np.full((3,2), 2)
print('New B Matrix ->', b)
print('\n')

print ('A x B -> ', np.matmul(a,b))
print('\n')

# Find the determinant
c = np.identity(3)
print('Matrix C -> ', c)
print('\n')

det_c = np.linalg.det(c)

print('Determinant C', det_c)
print('\n')

# Statistics

stats = np.array([[1,2,3],[4,5,6]])

np.min(stats)
np.max(stats, axis=1)
np.sum(stats, axis=0)

# Reorganizing Arrays

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,3))
print(after)

# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2,v1,v2])

# Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

np.hstack((h1,h2))

# Miscellaneous

# filedata = np.genfromtxt('data.txt', delimiter=',')
# filedata = filedata.astype('int32')
# print(filedata)

# (~((filedata > 50) & (filedata < 100)))
