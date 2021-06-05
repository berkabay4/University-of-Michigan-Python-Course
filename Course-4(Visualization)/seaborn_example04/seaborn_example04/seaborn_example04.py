### Plotting with date data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Line plots are often used to visualize data associated with real dates and times.
# These functions pass the data down in their original format to the underlying matplotlib functions,
#  and so they can take advantage of matplotlib’s ability to format dates in tick labels.

# But all of that formatting will have to take place at the matplotlib layer, 
# and you should refer to the matplotlib documentation to see how it works:

# Create DF
df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500),
                       value=np.random.randn(500).cumsum()))

g = sns.relplot(x="time", y="value", kind="line", data=df)

g.fig.autofmt_xdate()

plt.show()