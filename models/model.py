# === Imports ===
import pandas  as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import (r2_score, mean_absolute_error, mean_squared_error)
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# === DataFrame ===
macroeconomic_df = pd.read_csv(r'models\MacroEconomic_df.csv')

# === Data ===
X = macroeconomic_df[['Inflation', 'Key_rate', 'Brent_price']]
y = macroeconomic_df['USD_RUB']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
# === Model ===
pipe = Pipeline([
    ('scale', StandardScaler()),
    ('model', KNeighborsRegressor())
])

model = GridSearchCV(estimator=pipe, 
                     param_grid={'model__n_neighbors': [10]},
                     cv=3)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
# === Metrics ===
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred)

print("\n📊 Оценка модели:")
print(f"{'Метрика':<10} | {'Значение':>8}")
print("-" * 22)
print(f"{'R²':<10} | {r2:>8.2f}")
print(f"{'MAE':<10} | {mae:>8.2f}")
print(f"{'RMSE':<10} | {rmse:>8.2f}")
