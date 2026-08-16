# Week 5 — Gradient Descent from Scratch (Capstone)

## Industry context
A common way to prove real understanding of ML fundamentals — rather
than treating `model.fit()` as a black box — is to implement linear
regression's training loop by hand: define a loss function, derive its
gradient, and iteratively update parameters, then verify the result
against a trusted library implementation (`sklearn`). This task pulls
together every math topic from this phase into one working project:
matrix operations from Linear Algebra, gradients from Calculus, and a
convergence plot from Matplotlib.

## Core concepts

**Multi-feature linear model**
```
y_pred = X @ weights + bias
```

`X` is a feature matrix (rows = samples, columns = features) — the same
representation covered in Linear Algebra. Matrix multiplication computes
predictions for every sample at once, rather than looping row by row.

**Loss function — Mean Squared Error (MSE)**
```
MSE = (1/n) * sum((y_pred - y_actual)^2)
```

Squaring removes the sign of the error and penalizes larger mistakes
more heavily than small ones.

**Gradient of MSE (Calculus's chain rule, applied to a matrix)**
```
dW = (2/n) * X.T @ (y_pred - y_actual)
db = (2/n) * sum(y_pred - y_actual)
```

This is the same partial-derivative idea from the Calculus topic —
"how does the loss change if I move *this one* weight" — just computed
for every weight simultaneously via matrix multiplication instead of
one variable at a time.

**Parameter update rule**
```
weights -= learning_rate * dW
bias -= learning_rate * db
```

Move against the gradient (steepest increase), by a step sized by the
learning rate — moving in the *opposite* direction decreases the loss.

**Convergence isn't just "does the loss curve look flat"**
A loss curve can look fully converged (visually flat) while individual
parameters are still slowly drifting toward their optimum — different
parameters can converge at different rates. Here, weights matched
sklearn's closed-form solution almost immediately, but bias was still
measurably off (~0.50 difference) at 1000 iterations. Increasing to
3000 iterations let bias finish converging (~0.005 difference from
sklearn) without changing anything else in the model. Lesson: track the
actual parameter values, not just the loss curve, when deciding whether
training is done — and when in doubt, run longer and confirm the
numbers stop moving.

**Verifying against a trusted implementation**
Comparing the from-scratch result to `sklearn.linear_model.LinearRegression`
(which solves the same problem via a closed-form / different
optimization approach, not gradient descent) is the strongest available
check that the hand-derived math and code are correct — if both methods
converge to the same answer independently, the implementation is
almost certainly right.

## Task
`gradient_descent_from_scratch.py`
- Synthetic dataset: 200 samples, 3 features, generated from a known
  ground truth (`true_weights = [3.5, -2.0, 1.2]`, `true_bias = 5.0`)
  plus Gaussian noise — so the "correct answer" is known in advance.
- Full manual training loop (no library shortcuts): predictions, MSE
  loss (tracked every iteration for the convergence plot), gradients,
  parameter updates. 3000 iterations, `learning_rate=0.01`.
- Learned weights `[3.5039, -2.0295, 1.1924]` and bias `5.1105` compared
  directly against both the true generating parameters and sklearn's
  `LinearRegression` fit on the same data — final difference from
  sklearn: ~0.0003 on weights, ~0.005 on bias.
- Convergence plot (OO-style Matplotlib, reused from Week 1): MSE loss
  vs. iteration, showing the steep initial drop and long flat tail
  typical of gradient descent on a well-conditioned loss surface.

## Output
- `convergence_plot.png`
- Console output: true vs. learned vs. sklearn parameters, final loss,
  and explicit numerical differences between the from-scratch and
  sklearn results.