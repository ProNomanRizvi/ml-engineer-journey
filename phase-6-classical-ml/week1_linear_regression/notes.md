# Linear Regression

## Industry Context

Linear and logistic regression are where ML interviews start — not because
they're simple, but because interviewers use them to test whether you
understand what's actually happening inside a model, rather than just
knowing which sklearn class to call. Ridge and Lasso come up specifically
in questions about regularization, bias-variance tradeoff, and feature
selection. Residual analysis is expected too — knowing how to diagnose
whether a model's assumptions hold is part of what separates someone who
trained a model from someone who understands it.

## Core Concepts

**OLS (Ordinary Least Squares)**
Fits a line `ŷ = w₁x₁ + w₂x₂ + ... + b` by minimizing MSE directly via
the closed-form solution `w = (XᵀX)⁻¹ Xᵀy`. Fast on small datasets,
no hyperparameters needed.

**Loss Function**
```
MSE = (1/n) Σ(y - ŷ)²
RMSE = √MSE ← same units as target, more readable
R² = 1 - SS_res/SS_tot ← proportion of variance explained
```

**Regularization**

Ridge (L2) adds `λ Σw²` to the loss. Coefficients shrink toward zero but
never reach it. Good when all features carry some signal and you want
stability under multicollinearity.

Lasso (L1) adds `λ Σ|w|` to the loss. Some coefficients go exactly to
zero — it does feature selection automatically. Can be unstable when
predictors are correlated.

Elastic Net combines both penalties — useful when you want sparsity but
Ridge's stability.

The `λ` (alpha in sklearn) controls penalty strength. Too small → overfit.
Too large → underfit. Cross-validation finds the right value.

**Feature Scaling**
Ridge and Lasso penalize coefficient magnitude, so if features are on
different scales the penalty hits them unevenly. StandardScaler before
regularized regression is not optional — it's required for fair penalization.

**Assumptions (what gets tested in interviews)**
- Linearity: relationship between X and y is linear
- No multicollinearity: features should not be highly correlated with each other
- Homoscedasticity: residual variance stays constant across all predicted values
- Normality of residuals: residuals should be approximately normally distributed

## Tasks Completed

**Task 1 — `01_linear_regression.py`**
Trained LinearRegression, Ridge (alpha=1.0), and Lasso (alpha=0.1) on
California Housing (20,640 samples, 8 features, 80/20 split). Evaluated
RMSE and R² on test set. Compared feature coefficients across all three
models side by side.

Results:
```
Model RMSE R²
Linear 0.7456 0.5758
Ridge 0.7455 0.5759
Lasso 0.7833 0.5318
```

Lasso zeroed out `AveRooms` and `AveBedrms` at alpha=0.1 — both features
had real signal, so R² dropped. This is expected Lasso behavior, not a bug.

**Task 2 — `02_residual_analysis.py`**
Plotted residuals vs predicted values, residual distribution (histogram,
bins=50), and Q-Q plot via `scipy.stats.probplot`.