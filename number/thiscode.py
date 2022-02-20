import plotly.express as px
import csv

with open("csv2.csv") as f:
    df = csv.DictReader(f)
    figure = px.scatter(df, x="SizeofTV", y="Averagetime")
    figure.show()