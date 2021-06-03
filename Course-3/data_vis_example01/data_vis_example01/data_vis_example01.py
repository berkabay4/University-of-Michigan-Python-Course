import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Resize your Graph (dpi specifies pixel per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(5,3), dpi = 200)        # 5x3 inch, 200 dpi


## Line-1
# plt.plot(x,y, label = '2x', 
#          color = 'blue', 
#          linewidth = 2,
#          marker = 'o',
#          markersize = 10,
#          markeredgecolor = 'blue',
#          linestyle = '--')


#  Use shorthand notation
# fmt = '[color][marker][line]'
plt.plot(x,y, 'bo--', label = '2x')


## Line-2
# Select interval we want to plot points at
x2 = np.arange(0, 4, 0.5) 

# Plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2, 'r', label = 'X^2')

# Pkıt remainder of graph as a dot
plt.plot(x2[5:], x2[5:]**2, 'r--')

# Add a title (specify font parameters with fontdict)
plt.title('First Graph', 
          {'fontname' : 'Comic Sans MS', 'fontsize' : 15})

# X and Y Labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0, 1, 2, 3, 4])
# plt.yticks([0, 2, 4, 6, 8, 10])

# Add a Legend
plt.legend()

# Save your Graph (dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png', dpi = 300)

# Show plot
plt.show()


