import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print("Rows:", len(df))
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())