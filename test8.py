import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in('soumeet', 'JtsMoJEIOlWcoRhJv0uu') # Replace the username, and API key with your credentials.

trace = go.Bar(x=[2, 4, 6, 8, 10], y= [10, 12, 15, 18, 21])
data = [trace]
layout = go.Layout(title='A Simple Plot', width=800, height=640)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='test8.png')
'''
from IPython.display import Image
Image('a-simple-plot.png')
'''
