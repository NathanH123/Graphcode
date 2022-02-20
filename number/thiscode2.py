import plotly.express as px
import csv

with open("csv3.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="Roll No", y="Marks In Percentage")
    figure.show()