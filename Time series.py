import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from pandas import parser
from matplotlib import pyplot

#df = pd.read_csv("Data.csv")
series = Series.from_csv('Data.csv',header=0)
df = DataFrame(series)
#df = pd.read_csv('Data.csv',header=0)
df.plot()
pyplot.show()
