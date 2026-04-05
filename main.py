# === Import ===
from models.model import model

# === Functions ===
def input_data():
    while True:
        try:
            print()
            Inflation = float(input('Enter the inflation rate in Russia: '))
            Key_rate = float(input('Enter the key rate in Russia: '))
            Brent_price = float(input('Enter the brent price in Russia: '))
            return [[Inflation, Key_rate, Brent_price]]
        except ValueError:
            print("❌ Please enter valid numeric values.\n")

def model_predict(X):
    y = model.predict(X)
    return y

# === Main loop === 
if __name__ == '__main__':
    X = input_data()
    y = model_predict(X)
    print(f'The model assumes that the USD_RUB exchange rate is now: {y[0]:.2f} 💳')
