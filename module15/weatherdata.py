import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df["temperature"] = df["temperature"].astype(str)
df["temperature"] = df["temperature"].str.replace("(", "", regex=False)
df["temperature"] = df["temperature"].str.replace(")", "", regex=False)
df["temperature"] = pd.to_numeric(df["temperature"])

df["date"] = pd.to_datetime(df["year"].astype(str) + "/" + df["day"])

df["month"] = df["date"].dt.month

avg_temp = df["temperature"].mean()
print(f"\nAverage temperature (entire dataset): {avg_temp:.2f}°C")

monthly_avg = df.groupby("month")["temperature"].mean()
print("\nAverage temperature per month:")
print(monthly_avg)

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar", color="skyblue")
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.tight_layout()
plt.show()

hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("Hottest day record:")
print(hottest_day)

print("Coldest day record:")
print(coldest_day)

plt.figure(figsize=(12, 5))
plt.plot(df["date"], df["temperature"], color="orange")
plt.title("Temperature Change Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["month"].apply(get_season)

seasonal_avg = df.groupby("season")["temperature"].mean()
print("\nAverage temperature by season:")
print(seasonal_avg)

plt.figure(figsize=(6, 4))
seasonal_avg.plot(kind="bar", color=["blue", "green", "red", "orange"])
plt.title("Average Temperature by Season")
plt.ylabel("Temperature (°C)")
plt.grid(axis="y")
plt.tight_layout()
plt.show()
