# === Imports ===
import pandas as pd

# --- Serieses ---
from inflation import inflation_series
from key_rate import key_rate_series
from usd_rub import usd_rub_series
from brent_price import brent_price_series

# === DataFrame === 
macroeconomic_data = pd.concat([inflation_series, key_rate_series, brent_price_series, usd_rub_series], axis=1)
macroeconomic_data.rename(columns={
    0: 'Inflation',
    1: 'Key_rate',
    2: 'Brent_price',
    3: 'USD_RUB'
}, inplace=True)

print(macroeconomic_data)