import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
fig = px.scatter(df, x="number", y="iterations", title="Scatter Plot")
plotly.offline.plot(fig, filename = "./graphs/scatter_graph.html")