import numpy as np

output_matris = np.ones((5,5))
print('5x5 Ones Matrix -> ', output_matris)
print('\n')

z = np.zeros((3,3))
z[1,1] = 9
print('Middle Matrix -> ', z)
print('\n')

output_matris[1:-1,1:-1] = z
print('Output Matrix ->', output_matris)