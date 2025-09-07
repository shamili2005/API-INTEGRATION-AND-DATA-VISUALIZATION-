"""
Internship Task - 1
API Integration and Data Visualization
Using Python, Pandas, Matplotlib, Seaborn
"""

# ===============================
# 1. Import Libraries
# ===============================
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 2. API Integration
# (Using Coindesk Bitcoin API - No API key required)
# ===============================
url = "https://api.coindesk.com/v1/bpi/historical/close.json"

try:
    response = requests.get(url)
    response.raise_for_status()   # Raise error if request failed
    data = response.json()

    # Extract the 'bpi' dictionary (date: price)
    prices = data["bpi"]

    # Convert to DataFrame
    df = pd.DataFrame(list(prices.items()), columns=["Date", "Price"])
    df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime
    print("✅ Data successfully fetched from API.")

except Exception as e:
    print("⚠ Could not fetch data from API. Using sample data instead.")
    # Fallback sample data (offline mode)
    data = {
        "Date": pd.date_range("2023-01-01", periods=7),
        "Price": [16500, 16750, 17000, 16800, 17200, 17400, 17550]
    }
    df = pd.DataFrame(data)

# ===============================
# 3. Data Overview
# ===============================
print("\n📊 Sample Data:")
print(df.head())

# ===============================
# 4. Visualization 1: Line Chart
# ===============================
plt.figure(figsize=(10,5))
sns.lineplot(x="Date", y="Price", data=df, marker="o")
plt.title("Bitcoin Price Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 5. Visualization 2: Moving Average
# ===============================
df["MA_3"] = df["Price"].rolling(window=3).mean()

plt.figure(figsize=(10,5))
sns.lineplot(x="Date", y="Price", data=df, label="Daily Price", marker="o")
sns.lineplot(x="Date", y="MA_3", data=df, label="3-Day Moving Avg", marker="s")
plt.title("Bitcoin Price with Moving Average", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 6. Visualization 3: Distribution
# ===============================
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], kde=True, bins=10, color="orange")
plt.title("Distribution of Bitcoin Prices", fontsize=14)
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
