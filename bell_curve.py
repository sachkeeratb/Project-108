import csv
import pandas as pd
import plotly.figure_factory as pff

df = pd.read_csv("codebest.csv")

figure = pff.create_distplot([df["AvgRating"].tolist()],["AvgRating"],show_hist=False)
figure.show()