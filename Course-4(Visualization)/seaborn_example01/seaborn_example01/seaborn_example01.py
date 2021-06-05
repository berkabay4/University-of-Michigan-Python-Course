### Visualizing statistical relationships
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# sns.set_theme(style="darkgrid")
df_tips = sns.load_dataset("tips")
print(df_tips.head(5))

## Relating variables with scatter plots
sns.relplot(x = "total_bill", y = "tip", data = df_tips, col = 1)



sns.relplot(x = "total_bill", y = "tip", hue = "smoker", col = 3, data = df_tips)


# To emphasize the difference between the classes,
# and to improve accessibility, you can use a different marker style for each class:
sns.relplot(x = "total_bill", y = "tip", hue = "smoker", 
            style="time", col = 3, data = df_tips)



# In both cases, you can customize the color palette. 
# There are many options for doing so. Here, we customize a sequential palette 
# using the string interface to cubehelix_palette():
sns.relplot(x="total_bill", y="tip", hue="size", 
            palette="ch:r=-.5,l=.75", col = 4, data=df_tips);


# Unlike with matplotlib.pyplot.scatter(), the literal value of the variable is not 
# used to pick the area of the point.
#
# Instead, the range of values in data units is normalized into a range in area units. 
# This range can be customized:
sns.relplot(x="total_bill", y="tip", size="size", 
                   sizes=(15, 200), col = 5, data=df_tips);



