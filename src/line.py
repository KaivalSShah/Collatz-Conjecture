import plotly
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

x = ("number")
y = ("iterations")
df = pd.read_excel("./data/collatz.xlsx")
fig = px.line(df, x="number", y="iterations", title="Line Chart") 
fig.show()