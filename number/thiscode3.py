import plotly.express as px
import csv

with open("csv4.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="week", y="Coffee in ml")
    figure.show()