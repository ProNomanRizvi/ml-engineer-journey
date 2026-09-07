from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd


# ============================================================
# 1. LOAD DATA
# ============================================================

data = fetch_california_housing()

X = data.data
y = data.target

print("Dataset shape:", X.shape)
print("Target shape:", y.shape)


# ============================================================
# 2. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTrain samples:", X_train.shape[0])
print("Test samples :", X_test.shape[0])


# ============================================================
# 3. CREATE MODELS
# ============================================================

models = {
    "Linear": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.1)
}


# ============================================================
# 4. TRAIN + EVALUATE
# ============================================================

results = []

for name, model in models.items():

    # Train
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    results.append({
        "Model": name,
        "RMSE": rmse,
        "R²": r2
    })


# ============================================================
# 5. PRINT RESULTS
# ============================================================

results_df = pd.DataFrame(results)

print("\n" + "=" * 45)
print("MODEL PERFORMANCE")
print("=" * 45)

print(
    results_df.to_string(
        index=False,
        formatters={
            "RMSE": "{:.4f}".format,
            "R²": "{:.4f}".format
        }
    )
)


# ============================================================
# 6. FEATURE COEFFICIENTS
# ============================================================

coefficients_df = pd.DataFrame({
    "Feature": data.feature_names,
    "Linear": models["Linear"].coef_,
    "Ridge": models["Ridge"].coef_,
    "Lasso": models["Lasso"].coef_
})

print("\n" + "=" * 70)
print("FEATURE COEFFICIENTS")
print("=" * 70)

print(
    coefficients_df.to_string(
        index=False,
        formatters={
            "Linear": "{:.6f}".format,
            "Ridge": "{:.6f}".format,
            "Lasso": "{:.6f}".format
        }
    )
)