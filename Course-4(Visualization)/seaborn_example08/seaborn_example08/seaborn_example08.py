## Normalized histogram statistics

import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("ggplot")

# Load Dataframe
print("Info Penguins DF \n")
penguins = sns.load_dataset("penguins")

print(penguins.info(), "\n")
print("Penguins DataFrame \n")
print(penguins.head(10), "\n")


# Before we do, another point to note is that, when the subsets have unequal numbers of observations,
# comparing their distributions in terms of counts may not be ideal. 

# One solution is to normalize the counts using the stat parameter:
sns.displot(penguins, x="flipper_length_mm", hue="species", stat="density")

# By default, however, the normalization is applied to the entire distribution, 
# so this simply rescales the height of the bars. 

# By setting common_norm=False, each subset will be normalized independently:
sns.displot(penguins, x="flipper_length_mm", hue="species", stat="density", common_norm=False)

# Density normalization scales the bars so that their areas sum to 1. 
# As a result, the density axis is not directly interpretable. 
# Another option is to normalize the bars to that their heights sum to 1. 
# This makes most sense when the variable is discrete, but it is an option for all histograms:
sns.displot(penguins, x="flipper_length_mm", hue="species", stat="probability")

plt.show()