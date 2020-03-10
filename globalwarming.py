import pandas as pd
import numpy as np
import dateutil
import datetime
from matplotlib import pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('globalannualtemp.csv')


fig = go.Figure(go.Scatter(x = df['CO2 levels'], y = df['Year'],
                           name='CO2 Levels'))
fig.update_layout(title='CO2 Levels over the last 140 years',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)
fig.show()

