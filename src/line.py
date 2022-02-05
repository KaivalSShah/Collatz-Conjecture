import plotly
import pandas as pd
import plotly.express as px

df = pd.read_excel("./data/collatz.xlsx")
data = px.line(df, x="number", y="iterations", title="Line Chart") 
data.show()