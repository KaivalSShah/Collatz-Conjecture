import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

x = ("number")
y = ("iterations")
df = pd.read_excel("./data/collatz.xlsx")
print(df)
data = [go.Scatter(x=df[x], y=df[y])]
fig = go.Figure(data)
plotly.offline.plot(fig, filename = "./data/graph.html")