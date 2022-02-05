import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
data = px.scatter_polar(df, r="number", theta="iterations", title="Polar Chart")
fig = go.Figure(data)
plotly.offline.plot(fig, filename = "./data/polar_graph.html")