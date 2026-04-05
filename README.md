# 📈 USDT/RUB Exchange Rate Prediction Model

## 🧠 Overview

This project presents a simple macroeconomic model for predicting the USD/RUB exchange rate (proxy for USDT/RUB) using key economic indicators of the Russian economy. The model is based on a supervised machine learning approach and utilizes a k-Nearest Neighbors (k-NN) regression algorithm.

The primary objective is to explore the relationship between macroeconomic variables and exchange rate dynamics, and to provide a reproducible pipeline for training and inference.

---

## 📊 Data

The model relies on the following macroeconomic time series:

* **Inflation** — inflation rate in Russia
* **Key Rate** — Central Bank of Russia interest rate
* **Brent Price** — global oil benchmark price
* **USD/RUB** — exchange rate (target variable)

These series are combined into a single dataset:

```
MacroEconomic_df.csv
```

### 🏗️ Data Preparation

The dataset is constructed by concatenating individual time series:

```python
macroeconomic_data = pd.concat([
    inflation_series,
    key_rate_series,
    brent_price_series,
    usd_rub_series
], axis=1)
```

---

## ⚙️ Methodology

### 🔍 Feature Space

The model uses the following predictors:

* Inflation
* Key Rate
* Brent Oil Price

Target variable:

* USD/RUB exchange rate

---

### 🤖 Model

A machine learning pipeline is implemented using:

* **StandardScaler** — feature normalization
* **KNeighborsRegressor** — non-parametric regression model

The pipeline is wrapped in a **GridSearchCV** procedure for hyperparameter tuning.

```python
Pipeline([
    ('scale', StandardScaler()),
    ('model', KNeighborsRegressor())
])
```

### 🧪 Hyperparameters

| Parameter        | Value  |
| ---------------- | ------ |
| n_neighbors      | 10     |
| Cross-validation | 3-fold |

---

## 🏋️ Training Procedure

The dataset is split into training and testing subsets:

* Training set: 80%
* Test set: 20%

```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

---

## 📏 Evaluation Metrics

The model is evaluated using standard regression metrics:

* **R² (coefficient of determination)**
* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**

Example output:

```
📊 Model Evaluation:
Metric     |   Value
----------------------
R²         |    0.XX
MAE        |    X.XX
RMSE       |    X.XX
```

---

## 🚀 Usage

### 1. Train the Model

Run the training script:

```bash
python train_model.py
```

---

### 2. Run Inference

Execute the prediction script:

```bash
python main.py
```

You will be prompted to enter:

* Inflation rate
* Key rate
* Brent price

Example:

```
Enter the inflation rate in Russia: 7.5
Enter the key rate in Russia: 16
Enter the brent price in Russia: 85
```

Output:

```
The model assumes that the USD_RUB exchange rate is now: XX.XX 💳
```

---

## 🗂️ Project Structure

```
project/
│
├── models/
│   ├── MacroEconomic_df.csv
│   └── model.py
│
├── data_sources/
│   ├── inflation.py
│   ├── key_rate.py
│   ├── usd_rub.py
│   └── brent_price.py
│
├── main.py
└── README.md
```

---

## ⚠️ Limitations

* The model uses a limited feature space and does not account for:

  * geopolitical risks
  * market sentiment
  * monetary policy expectations
* k-NN does not extrapolate well outside observed data ranges
* Hyperparameter tuning is minimal

---

## 🔮 Future Work

* Incorporation of additional macroeconomic and financial indicators
* Time-series models (ARIMA, LSTM, Transformer-based approaches)
* Feature engineering and lag variables
* Model comparison and ensemble methods

---

## 📌 Disclaimer

This project is intended for research and educational purposes only.
It should not be used for financial decision-making or trading.

---

## 👤 Author

Independent research project in applied machine learning and macroeconomic modeling.
