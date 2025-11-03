# === Import ===
import pandas as pd

# === Data ===
key_rate_data = pd.read_csv('data\inflation_and_the_key_rate.csv', sep=';') # <-- parsing of official data of the Central Bank of Russia

key_rate_close = key_rate_data['Key_rate']# <-- we take only the necessary information

# === Create a list and sort it ===
key_rate_values = key_rate_close.tolist()

key_rate_final = [float(str(key_rate).replace(',', '.').strip()) for key_rate in key_rate_values]

# === Create a pd.Series ===
key_rate_series = pd.Series(key_rate_final)

