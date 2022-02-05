import plotly
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
data = px.scatter_polar(df, r="number", theta="iterations", title="Polar Chart")
data.show()