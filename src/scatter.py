import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
data = px.scatter(df, x="number", y="iterations", title="Scatter Plot")
fig = go.Figure(data)
plotly.offline.plot(fig, filename = "./data/scatter_graph.html")