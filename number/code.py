import plotly.express as px
import csv

with open("csv1.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="Temperature", y="Ice-cream")
    figure.show()