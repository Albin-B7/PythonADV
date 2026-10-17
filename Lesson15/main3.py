import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', skipinitialspace=True)

df.columns = df.columns.str.strip()

df['temperature'] = (
    df['temperature'].astype(str)
    .str.strip()
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

df['temperature'] = pd.to_numeric(
    df['temperature'], errors='coerce'
)

df['date'] = pd.to_datetime(
    df['year'].astype(str) + '/' + df['day'].astype(str),
    format='%Y/%m/%d',
    errors='coerce'
)

df = df.dropna(subset=['date', 'temperature'])

hottest_day = df.loc[df['temperature'].idxmax()]
coldest_day = df.loc[df['temperature'].idxmin()]

print("Hottest day:")
print("Date:", hottest_day['date'].strftime('%Y-%m-%d'))
print("Temperature:", hottest_day['temperature'], "°C")

print("\nColdest day:")
print("Date:", coldest_day['date'].strftime('%Y-%m-%d'))
print("Temperature:", coldest_day['temperature'], "°C")

extreme_days = pd.DataFrame({
    'Day': ['Hottest day', 'Coldest day'],
    'Temperature': [
        hottest_day['temperature'],
        coldest_day['temperature']
    ]
})

plt.figure(figsize=(9, 6))

bars = plt.bar(
    extreme_days['Day'],
    extreme_days['Temperature'],
    color=['tomato', 'skyblue']
)

plt.title('Hottest and Coldest Days', fontsize=16)
plt.xlabel('Day', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

plt.bar_label(bars, fmt='%.2f °C', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()