import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('csv/sharing_bike_test.csv')

df["year"] = pd.to_datetime(df["datetime"]).dt.year
df["month"] = pd.to_datetime(df["datetime"]).dt.month
df["day"] = pd.to_datetime(df["datetime"]).dt.day
df["hour"] = pd.to_datetime(df["datetime"]).dt.hour
df["weekday"] = pd.to_datetime(df["datetime"]).dt.weekday

print(df["humidity"])
