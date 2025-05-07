import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

import kagglehub

# Download latest version
path = kagglehub.dataset_download("ulrikthygepedersen/nike-shoes-sales")

print("Path to dataset files:", path)

df = pd.read_csv(path + "/nike_shoes_sales.csv")
print(df.columns)

filtered_data = df[["product_name", "sale_price"]]
print(filtered_data)

grouped_data = filtered_data.groupby("product_name").mean().reset_index()

plt.figure(figsize=(10, 5))
plt.bar(grouped_data["product_name"][:10], grouped_data["sale_price"][:10], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Product Name")
plt.ylabel("Average Sale Price")
plt.title("Average Nike Shoes Sales Prices")
plt.show()
