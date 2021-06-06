## Conditioning on other variables
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("ggplot")

# Load Penguins Dataframe
penguins = sns.load_dataset("penguins")
print("Penguins DataFrame \n")
print(penguins.head(15), "\n")

# Once you understand the distribution of a variable, the next step is often to ask 
# whether features of that distribution differ across other variables in the dataset.
sns.displot(penguins, x="flipper_length_mm", hue="species").set(
    title = "Flipper lenght by species" , xlabel = "Flipper Lenght[mm]", ylabel = "Count")


#By default, the different histograms are “layered” on top of each other and, 
#in some cases, they may be difficult to distinguish. One option is to change 
#the visual representation of the histogram from a bar plot to a “step” plot:
sns.displot(penguins, x="flipper_length_mm", hue="species", element="step").set(
    title = "Flipper lenght by species [Step Hist.]" , xlabel = "Flipper Lenght[mm]", ylabel = "Count")

# Alternatively, instead of layering each bar, they can be “stacked”, or moved vertically. 
# In this plot, the outline of the full histogram will match the plot with only a single variable:

# Change palette
sns.set_palette("pastel")

sns.displot(penguins, x="flipper_length_mm", hue="species", multiple="stack").set(
    title = "Flipper lenght by species [Stack Hist.]" , xlabel = "Flipper Lenght[mm]", ylabel = "Count")

# Change palette
sns.set_palette("bright")

# Poly Hist.
sns.displot(penguins, x="flipper_length_mm", hue="species", element="poly").set(
    title = "Flipper lenght by species [Poly Hist.]" , xlabel = "Flipper Lenght[mm]", ylabel = "Count")

plt.show()

# The stacked histogram emphasizes the part-whole relationship between the variables, 
# but it can obscure other features (for example, it is difficult to determine the mode of 
# the Adelie distribution.) 

# Another option is “dodge” the bars, which moves them horizontally and reduces their width. 
# This ensures that there are no overlaps and that the bars remain comparable in terms of height.
# But it only works well when the categorical variable has a small number of levels:
sns.displot(penguins, x="flipper_length_mm", hue="sex", multiple="dodge").set(
    title = "Flipper lenght by sex [Dodge Hist.]" , xlabel = "Flipper Lenght[mm]", ylabel = "Count")



# Because displot() is a figure-level function and is drawn onto a FacetGrid, 
# it is also possible to draw each individual distribution in a separate subplot by assigning 
# the second variable to col or row rather than (or in addition to) hue.
sns.displot(penguins, x="flipper_length_mm", col="species", hue = "sex", multiple="dodge")


plt.show()

