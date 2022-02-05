import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
fig = px.line(df, x="number", y="iterations", title="Line Chart") 
plotly.offline.plot(fig, filename = "./data/line_chart_graph.html")