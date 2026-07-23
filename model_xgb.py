from xgboost import XGBRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error
)
xgb = XGBRegressor(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    random_state=42
)
xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_test)

print(
    "R2 =",
    r2_score(y_test, y_pred)
)

print(
    "MAE =",
    mean_absolute_error(y_test, y_pred)
)