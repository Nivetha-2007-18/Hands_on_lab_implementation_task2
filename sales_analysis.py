import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print("Total sales:", df["Sales"].sum())
print("Total profit:", df["Profit"].sum())

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(category_sales)
print(region_sales)

category_sales.sort_values().plot(kind="barh", title="Sales by Category")
plt.tight_layout()
plt.show()

df.groupby("Month")["Sales"].sum().plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.tight_layout()
plt.show()
