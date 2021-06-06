### Visualizing distributions of data

# Techniques for distribution visualization can provide quick 
# answers to many important questions. What range do the observations cover?
# What is their central tendency? Are they heavily skewed in one direction? Are there significant outliers? 
# Do the answers to these questions vary across subsets defined by other variables?

# The distributions module contains several functions designed to answer questions such as these. 
# The axes-level functions are histplot(), kdeplot(), ecdfplot(), and rugplot().
# They are grouped together within the figure-level displot(), jointplot(), and pairplot()

import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load Dataframe
penguins = sns.load_dataset("penguins")
print("Penguins DataFrame \n")
print(penguins.head(5), "\n")

## Plotting univariate histograms

# Perhaps the most common approach to visualizing a distribution is the histogram. 
# This is the default approach in displot(), which uses the same underlying code as histplot().
sns.displot(penguins, x="flipper_length_mm").set(
    title = "Hist. Binwidth = Default", xlabel = "Flipper Lenght [mm]", ylabel ="Count")

# This plot immediately affords a few insights about the flipper_length_mm variable. 
# For instance, we can see that the most common flipper length is about 195 mm, but 
# the distribution appears bimodal, so this one number does not represent the data well

## Chosing the bin size 

# The size of the bins is an important parameter, and using the wrong bin size can mislead by obscuring 
# important features of the data or by creating apparent features out of random variability.
sns.displot(penguins, x="flipper_length_mm", binwidth=3). set(
    title = "Hist. Binwidth = 3", xlabel = "Flipper Lenght [mm]", ylabel ="Count")

# n other circumstances, it may make more sense to specify the number of bins, 
# rather than their size:
# sns.displot(penguins, x="flipper_length_mm", bins=20)
plt.show()

# Load Tips Dataframe
tips = sns.load_dataset("tips")

print("Tips DataFrame \n")
print(tips.head(5), "\n")



# One example of a situation where defaults fail is when the variable takes a 
# relatively small number of integer values. In that case, the default bin width 
# may be too small, creating awkward gaps in the distribution:
sns.displot(tips, x="size").set(
    title = "Tips Binwidth = Default", xlabel = "Size", ylabel ="Count")

# One approach would be to specify the precise bin breaks by passing an array to bins:
# sns.displot(tips, x="size", bins=[1, 2, 3, 4, 5, 6, 7])

# This can also be accomplished by setting discrete=True, 
# which chooses bin breaks that represent the unique values in a dataset with 
# bars that are centered on their corresponding value.
sns.displot(tips, x="size", discrete=True).set(
    title = "Tips Hist. discrete = True", xlabel = "Size", ylabel ="Count")


# It’s also possible to visualize the distribution of a categorical variable using the logic 
# of a histogram. Discrete bins are automatically set for categorical variables, 
# but it may also be helpful to “shrink” the bars slightly to emphasize the 
# categorical nature of the axis:
sns.displot(tips, x="day", shrink=.8).set(
    title = "Tips Hist. shrink = .8", xlabel = "Days", ylabel ="Count")


plt.show()