import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', skipinitialspace=True)

df.columns = df.columns.str.strip()

df['temperature'] = (
    df['temperature']
    .astype(str)
    .str.strip()
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

df['date'] = pd.to_datetime(
    df['year'].astype(str) + '/' + df['day'].astype(str),
    format='%Y/%m/%d',
    errors='coerce'
)

filtered_df = (
    df.groupby('year')['temperature']
    .mean()
    .reset_index()
)

filtered_df = filtered_df.sort_values(
    by='temperature',
    ascending=False
)

plt.figure(figsize=(14, 8))

bars = plt.bar(
    filtered_df['year'],
    filtered_df['temperature'],
    color='skyblue'
)

plt.title('Average Temperature per Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.8)

plt.bar_label(bars, fmt='%.2f', fontsize=9, color='black')

plt.tight_layout()
plt.show()