import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ulrikthygepedersen/nike-shoes-sales")

print("Path to dataset files:", path)

df = pd.read_csv(path + "/nike_shoes_sales.csv")
print(df.columns)
print(df.shape)
print(df.info())
print(df.describe())
print("Null rows", df.isnull().sum())

filtered_data = df[["product_name", "sale_price"]]
print(filtered_data)

avg_ratings = df.groupby("product_name")["rating"].mean().reset_index()
print("Середні рейтинги продуктів:")
print(avg_ratings)

grouped_data = filtered_data.groupby("product_name").mean().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(grouped_data["product_name"][:10], grouped_data["sale_price"][:10], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Product Name")
plt.ylabel("Average Sale Price")
plt.title("Average Nike Shoes Sales Prices")
plt.show()

grouped_data_sorted = grouped_data.sort_values(by="sale_price")

plt.figure(figsize=(10, 5))
plt.plot(grouped_data_sorted["product_name"][:10], grouped_data_sorted["sale_price"][:10], marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Product Name")
plt.ylabel("Average Sale Price")
plt.title("Nike Shoes Sales Prices (Line Chart)")
plt.grid(True)
plt.show()

filtered_pie_data = df[["product_name", "sale_price"]].groupby("product_name").sum()

plt.figure(figsize=(8, 8))
plt.pie(filtered_pie_data["sale_price"][:10], labels=filtered_pie_data.index[:10], autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'gold'])
plt.title("Nike Shoes Sales Distribution")
plt.show()
