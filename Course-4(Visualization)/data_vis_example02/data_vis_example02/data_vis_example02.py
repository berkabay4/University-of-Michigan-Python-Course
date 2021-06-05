import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bar Chart

labels = ['A', 'B', 'C']
values = [1, 4, 5]

bars = plt.bar(labels, values)


# bars[0].set_hatch('/')
# bar[1].set_hatch('o')
# bars[2].set_hatch('*')

# or

patterns = ['/', 'o', '*']

for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.figure(figsize = (6,4))

plt.show()

