import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load DF
print("Dots Data Frame \n")
dots = sns.load_dataset("dots").query("align == 'dots'")
print(dots.head(10), "\n")


# The default colormap and handling of the legend in lineplot()
# also depends on whether the hue semantic is categorical or numeric:
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            kind="line", data=dots);

# It may happen that, even though the hue variable is numeric, 
# it is poorly represented by a linear color scale.
 
# That’s the case here, where the levels of the hue variable are logarithmically scaled. 
# You can provide specific color values for each line by passing a list or dictionary:
palette = sns.cubehelix_palette(light=.8, n_colors=6)
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            palette=palette,
            kind="line", data=dots);


# Or you can alter how the colormap is normalized:
from matplotlib.colors import LogNorm
palette = sns.cubehelix_palette(light=.7, n_colors=6)
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            hue_norm=LogNorm(),
            kind="line",
            data=dots.query("coherence > 0"));


# The third semantic, size, changes the width of the lines:
sns.relplot(x="time", y="firing_rate",
            size="coherence", style="choice",
            kind="line", data=dots);

# While the size variable will typically be numeric, 
# it’s also possible to map a categorical variable with the width of the lines. 
# Be cautious when doing so, because it will be difficult to distinguish much more than 
# “thick” vs “thin” lines. owever, dashes can be hard to perceive when lines have high-frequency variability, 
# so using different widths may be more effective in that case:
sns.relplot(x="time", y="firing_rate",
           hue="coherence", size="choice",
           palette=palette,
           kind="line", data=dots);

plt.show()