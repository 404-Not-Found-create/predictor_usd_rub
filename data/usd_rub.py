# === Imports ===
import yfinance as yf 
import pandas as pd 

# === Data ===
usd_rub_data = yf.download('USDRUB=X', start='2015-09-01', end='2025-01-01')# <-- we take usd_rub for a certain period

usd_rub_close = usd_rub_data[('Close', 'USDRUB=X')]# <-- we take only the necessary information

usd_rub_monthly = usd_rub_close.resample('M').mean()# <-- divide by months and take the average value.print(USD_RUB)

# === Create a list and sort it ===
usd_rub_values = usd_rub_monthly.tolist()
usd_rub_values.reverse()

usd_rub_final = [round(usd, 2) for usd in usd_rub_values]

# === Create a pd.Series ===
usd_rub_series = pd.Series(usd_rub_final)

