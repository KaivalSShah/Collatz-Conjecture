import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

x = ("number")
y = ("iterations")
df = pd.read_excel("./data/collatz.xlsx")
data = px.scatter(df, x="number", y="iterations")
fig = go.Figure(data)
plotly.offline.plot(fig, filename = "./data/graph.html")