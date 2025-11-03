# === Imports ===
import yfinance as yf 
import pandas as pd

# === Data ===
brent_price_data = yf.download('CL=F', start='2015-09-01', end='2025-01-01')# <-- we take brent_price for a certain period

brent_price_close = brent_price_data[('Close', 'CL=F')]# <-- we take only the necessary information

brent_price_mountly = brent_price_close.resample('M').mean()# <-- divide by months and take the average value.

# === Create a list and sort it ===
brent_price_values = brent_price_mountly.tolist()
brent_price_values.reverse()

brent_price_final = [round(brent_price, 2) for brent_price in brent_price_values]

# === Create pd.Series ===
brent_price_series = pd.Series(brent_price_final)

