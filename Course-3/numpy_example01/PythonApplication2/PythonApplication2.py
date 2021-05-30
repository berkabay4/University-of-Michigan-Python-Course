import numpy as np

a = np.array([1,2,3])
b = np.array([[3.33, 5.26, 7.00],[11.32, 44.61, 25.28]])

print("Matris A ->", a)
print("Matris B ->", b)
print('\n')

# Get dimension
print("A Dimension =", a.ndim)
print("B Dimension = ", b.ndim)
print('\n')

# Get Type
print("MatisA type ->", a.dtype)
print("MatrisB type ->", b.dtype)


print("A Item size [integer] -> ", a.itemsize)
print("A size ->", a.size)
print('\n')

print("Total Size = size * itemsize \n") # or a.nbytes
print("Total Size [A] = ", a.nbytes)
print('\n')


print("B Item size [float]->", b.itemsize)
print("B size ->", b.size)
print('\n')

print("Total Size = size * itemsize \n") # or b.nbytes
print("Total Size [B] = ", b.nbytes)
print('\n')

