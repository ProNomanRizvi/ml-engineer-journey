# gradient_descent_from_scratch.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# ============================================================
# 1. CREATE FAKE MULTI-FEATURE DATASET
# ============================================================

np.random.seed(42)

n_samples = 200

# We have 200 samples and 3 input features.
# Multiplying by 10 makes every feature fall roughly between 0 and 10.
X = np.random.rand(n_samples, 3) * 10

# These are the real parameters used to generate y.
# Our gradient descent model does not know these values.
true_weights = np.array([3.5, -2.0, 1.2])
true_bias = 5.0

# Random noise makes the dataset more realistic.
# A real-world target usually contains some unexplained variation.
noise = np.random.normal(0, 1, n_samples)

# Matrix multiplication calculates:
# y = 3.5*x1 - 2.0*x2 + 1.2*x3 + 5 + noise
y = X @ true_weights + true_bias + noise


# ============================================================
# 2. INITIALIZE MODEL PARAMETERS
# ============================================================

# Start with zero weights so the model initially has no
# knowledge about the relationship between X and y.
weights = np.zeros(3)

# Start the intercept at zero for the same reason.
bias = 0.0

# Learning rate controls how large each parameter update is.
# 0.01 is small enough to give stable convergence here.
learning_rate = 0.01

# More iterations give gradient descent more opportunities
# to reduce the error and approach the optimal parameters.
n_iterations = 3000

# We store every loss so we can visualize convergence later.
loss_history = []


# ============================================================
# 3. GRADIENT DESCENT TRAINING
# ============================================================

for iteration in range(n_iterations):

    # --------------------------------------------------------
    # STEP 1: Make predictions
    # --------------------------------------------------------

    # Matrix multiplication computes predictions for all
    # 200 samples at once:
    #
    # y_pred = X1*w1 + X2*w2 + X3*w3 + bias
    y_pred = X @ weights + bias


    # --------------------------------------------------------
    # STEP 2: Calculate prediction error
    # --------------------------------------------------------

    # The error tells us how far each prediction is from
    # the actual target value.
    error = y_pred - y


    # --------------------------------------------------------
    # STEP 3: Calculate MSE loss
    # --------------------------------------------------------

    # Squaring removes negative signs and penalizes
    # larger prediction errors more strongly.
    mse = np.mean(error ** 2)

    # Store the loss so we can plot training convergence.
    loss_history.append(mse)


    # --------------------------------------------------------
    # STEP 4: Calculate gradients
    # --------------------------------------------------------

    # Gradient with respect to each weight:
    #
    # dW = (2/n) * X.T @ (y_pred - y)
    #
    # X.T changes the matrix orientation so that each
    # feature receives its own gradient.
    dW = (2 / n_samples) * (X.T @ error)

    # Gradient with respect to bias:
    #
    # db = (2/n) * sum(y_pred - y)
    #
    # Bias affects every prediction equally, so its gradient
    # is the average error multiplied by 2.
    db = (2 / n_samples) * np.sum(error)


    # --------------------------------------------------------
    # STEP 5: Update parameters
    # --------------------------------------------------------

    # We move in the opposite direction of the gradient
    # because the gradient points toward increasing loss.
    weights -= learning_rate * dW
    bias -= learning_rate * db


# ============================================================
# 4. TRAINING RESULTS
# ============================================================

print("=" * 60)
print("FROM-SCRATCH GRADIENT DESCENT RESULTS")
print("=" * 60)

print("\nTrue weights:")
print(true_weights)

print("\nLearned weights:")
print(weights)

print("\nTrue bias:")
print(true_bias)

print("\nLearned bias:")
print(bias)

print("\nFinal MSE loss:")
print(loss_history[-1])


# ============================================================
# 5. CONVERGENCE PLOT
# ============================================================

# OO-style Matplotlib:
# fig represents the whole figure,
# ax represents the plotting area.
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(loss_history)

ax.set_title("Gradient Descent Convergence")
ax.set_xlabel("Iteration")
ax.set_ylabel("MSE Loss")

# Grid makes it easier to visually inspect how quickly
# the loss decreases.
ax.grid(True)

fig.tight_layout()

# Save the plot so it can be included in the project/README.
plt.savefig("convergence_plot.png")

plt.show()


# ============================================================
# 6. BONUS: COMPARE WITH SKLEARN
# ============================================================

sk_model = LinearRegression()

# sklearn calculates the optimal linear regression parameters
# using a closed-form optimization approach rather than our
# iterative gradient descent loop.
sk_model.fit(X, y)

print("\n" + "=" * 60)
print("SKLEARN LINEAR REGRESSION")
print("=" * 60)

print("\nSklearn weights:")
print(sk_model.coef_)

print("\nSklearn bias:")
print(sk_model.intercept_)


# ============================================================
# 7. COMPARE RESULTS
# ============================================================

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

print("\nDifference between scratch and sklearn weights:")
print(weights - sk_model.coef_)

print("\nDifference between scratch and sklearn bias:")
print(bias - sk_model.intercept_)