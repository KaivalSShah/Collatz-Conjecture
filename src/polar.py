import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
fig = px.scatter_polar(df, r="number", theta="iterations", title="Polar Chart")
plotly.offline.plot(fig, filename = "./data/polar_graph.html")