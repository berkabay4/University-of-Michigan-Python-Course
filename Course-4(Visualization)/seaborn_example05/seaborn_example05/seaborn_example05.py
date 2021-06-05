### Showing multiple relationships with facets
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")

# Show all DF
print("Tips DF \n")
print(tips.head(10), "\n")

print("FMRI DF \n")
print(fmri.head(10), "\n")



sns.relplot(x="total_bill", y="tip", hue="smoker",
            col="time", data=tips);

# You can also show the influence two variables this way: 
# one by faceting on the columns and one by faceting on the rows.
# As you start adding more variables to the grid, you may want to decrease 
# the figure size. Remember that the size FacetGrid is parameterized by 
# the height and aspect ratio of each facet:

sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", estimator=None, data=fmri);

# When you want to examine effects across many levels of a variable, 
# it can be a good idea to facet that variable on the columns and then 
# “wrap” the facets into the rows:

sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=3, aspect=.75, linewidth=2.5,
            kind="line", data=fmri.query("region == 'frontal'"));

plt.show()