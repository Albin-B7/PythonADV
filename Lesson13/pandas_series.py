import pandas as pd

products = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pineapples']

sales = [150, 200, 180, 90, 60]

sales_series = pd.Series(sales, index=products)

print(sales_series)

print(sales_series['Grapes'])

total_sum = sales_series.sum()
print(total_sum)

best_selling_products = sales_series.idxmax()
print(f"Best selling products: [best_selling_products")

