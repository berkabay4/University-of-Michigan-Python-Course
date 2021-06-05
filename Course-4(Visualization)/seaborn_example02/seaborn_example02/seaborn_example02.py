## Emphasizing continuity with line plots
# Scatter plots are highly effective, but there is no universally optimal type of visualisation. 
# Instead, the visual representation should be adapted for the specifics of the 
# dataset and to the question you are trying to answer with the plot.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# Create DF
print("Data Frame - 1 \n")
df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
print(df.head(5))

# Draw Lineplot
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.fig.autofmt_xdate()

# Because lineplot() assumes that you are most often trying to draw y as a function of x,
# the default behavior is to sort the data by the x values before plotting. 
# However, this can be disabled:
print("Data Frame - 2 \n")
df2 = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
print(df2.head(5))

sns.relplot(x="x", y="y", sort=False, kind="line", data=df2);
plt.show()

## Aggregation and representing uncertainty

# More complex datasets will have multiple measurements for the same value 
# of the x variable. The default behavior in seaborn is to aggregate 
# the multiple measurements at each x value by plotting the mean and the 
# 95% confidence interval around the mean:
print("Data Frame - 3 \n")
fmri = sns.load_dataset("fmri")
print(fmri.head(5))

sns.relplot(x="timepoint", y="signal", kind="line", data=fmri);

# The confidence intervals are computed using bootstrapping, which can be 
# time-intensive for larger datasets. It’s therefore possible to disable them:
sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri);

# Especially with larger data, is to represent the spread of the distribution 
# at each timepoint by plotting the standard deviation instead of a confidence interval:
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);

# To turn off aggregation altogether, set the estimator parameter to 
# None This might produce a strange effect when the data have multiple observations at each point.
sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);

plt.show()

## Plotting subsets of data with semantic mappings

# Using semantics in lineplot() will also determine how the data get aggregated. 
# For example, adding a hue semantic with two levels splits the plot into two lines and error bands, 
# coloring each to indicate which subset of the data they correspond to.
sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri);

# Adding a style semantic to a line plot changes the pattern of 
# dashes in the line by default:
sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            kind="line", data=fmri);

# But you can identify subsets by the markers used at each observation, 
# either together with the dashes or instead of them:
sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            dashes=False, markers=True, kind="line", data=fmri);


# When you are working with repeated measures data 
# (that is, you have units that were sampled multiple times), 
# you can also plot each sampling unit separately without distinguishing 
# them through semantics. This avoids cluttering the legend:
sns.relplot(x="timepoint", y="signal", hue="region",
            units="subject", estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));

plt.show()

