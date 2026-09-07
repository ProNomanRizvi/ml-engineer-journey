from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ============================================================
# 1. LOAD DATA
# ============================================================

data = fetch_california_housing()

X = data.data
y = data.target


# ============================================================
# 2. TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 3. TRAIN LINEAR REGRESSION
# ============================================================

model = LinearRegression()

model.fit(X_train, y_train)


# ============================================================
# 4. MAKE PREDICTIONS
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 5. CALCULATE RESIDUALS
# ============================================================

residuals = y_test - y_pred


# ============================================================
# 6. PRINT RESIDUAL STATISTICS
# ============================================================

residual_mean = np.mean(residuals)
residual_std = np.std(residuals)
residual_min = np.min(residuals)
residual_max = np.max(residuals)

print("=" * 50)
print("RESIDUAL ANALYSIS")
print("=" * 50)

print(f"Residual Mean   : {residual_mean:.6f}")
print(f"Residual Std    : {residual_std:.6f}")
print(f"Residual Range  : {residual_min:.6f} to {residual_max:.6f}")


# ============================================================
# 7. CREATE SINGLE FIGURE
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))


# ============================================================
# PLOT 1 — RESIDUALS VS PREDICTED
# ============================================================

axes[0].scatter(
    y_pred,
    residuals,
    alpha=0.4
)

axes[0].axhline(
    y=0,
    color="red",
    linestyle="--"
)

axes[0].set_title("Residuals vs Predicted")
axes[0].set_xlabel("Predicted Values")
axes[0].set_ylabel("Residuals")


# ============================================================
# PLOT 2 — RESIDUAL DISTRIBUTION
# ============================================================

axes[1].hist(
    residuals,
    bins=50
)

axes[1].set_title("Residual Distribution")
axes[1].set_xlabel("Residuals")
axes[1].set_ylabel("Frequency")


# ============================================================
# PLOT 3 — Q-Q PLOT
# ============================================================

stats.probplot(
    residuals,
    dist="norm",
    plot=axes[2]
)

axes[2].set_title("Q-Q Plot")


# ============================================================
# 8. FINAL LAYOUT
# ============================================================

plt.tight_layout()


# ============================================================
# 9. SAVE FIGURE
# ============================================================

plt.savefig(
    "residual_analysis.png",
    dpi=150,
    bbox_inches="tight"
)


# ============================================================
# 10. DISPLAY FIGURE
# ============================================================

plt.show()
