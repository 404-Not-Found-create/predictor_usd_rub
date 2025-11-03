# === Import ===
import pandas as pd

# === Data ===
inflation_data = pd.read_csv('data\inflation_and_the_key_rate.csv', sep=';') # <-- parsing of official data of the Central Bank of Russia

inflation_close = inflation_data['Inflation']# <-- we take only the necessary information

# === Create a list and sort it ===
inflation_values = inflation_close.tolist()

inlation_final = [float(str(inf).replace(',', '.').strip()) for inf in inflation_values]

# === Create a pd.Series ===
inflation_series = pd.Series(inlation_final)

