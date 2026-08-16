# Week 3-5 — Calculus + Statistics

## Industry context
Entry-level ML math needs calculus (derivatives, chain rule) enough to
understand backpropagation conceptually, and probability/statistics
(distributions, Bayes' theorem, hypothesis testing) enough to read a
model paper and diagnose why a model is underfitting vs. overfitting —
not a graduate-level treatment of either.

---

# Calculus

## Industry context
Multivariate calculus — partial derivatives and the chain rule — is the
bedrock of backpropagation: every neural network is a stack of composite
functions, and training it means computing how the loss changes with
respect to every single weight, layer by layer, backward through that
stack.

## Core concepts

**Derivative**
The rate of change / slope of a function at a specific point. In ML, the
loss function's derivative with respect to a weight tells us: if I nudge
this weight up or down, does the loss go up or down? That single
question is the entire basis of Gradient Descent.

**Numerical vs. symbolic derivative**
- Symbolic: derived algebraically from a known formula (e.g.
  `d/dx(x^2) = 2x`) — exact.
- Numerical: approximated directly from the function using a small step
  `h`. Central difference — `(f(x+h) - f(x-h)) / (2h)` — is more
  accurate than the naive forward-difference version and was used here
  to numerically verify every symbolic derivative in this file.

**Chain rule**
For a composite function `f(g(x))`:
`d/dx f(g(x)) = f'(g(x)) * g'(x)`.
Neural network layers are literally nested composite functions
(`layer3(layer2(layer1(x)))`), so backpropagation is chain rule applied
at scale, layer by layer, to get the gradient of the loss with respect
to every weight in the network.

**Partial derivative**
When a function has multiple variables, the partial derivative with
respect to one variable treats all the others as constants. Real models
have thousands of weights — a partial derivative answers "how does the
loss change if I move *this one* weight, holding everything else fixed."

**Gradient**
The vector of all partial derivatives of a function
(`∇f = [∂f/∂x, ∂f/∂y, ...]`). It points in the direction of steepest
*increase*. Gradient Descent moves in the *opposite* direction (negative
gradient) to decrease the loss as fast as possible:
`new_weight = old_weight - learning_rate * gradient`.

**Sigmoid derivative**
`sigmoid(x) = 1 / (1 + e^-x)` squashes any real number into `(0, 1)`,
making it usable as a probability-like output between layers. Its
derivative simplifies algebraically to a remarkably clean form:
`sigmoid(x) * (1 - sigmoid(x))`. This matters practically — once
sigmoid(x) is computed in the forward pass, its derivative comes almost
for free during the backward pass, which is exactly why it's convenient
in backpropagation.

## Task
`calculus_basics.py`
- Basic derivative of `f(x) = x^2`, verified numerically via central
  difference.
- Chain rule on a composite function `f(g(x))` where `g(x) = 2x + 1` and
  `f(u) = u^2`, verified against the numerical derivative of the full
  composite function.
- Partial derivatives of `f(x, y) = x^2 + y^2`.
- Gradient as a vector of both partials, followed by a working Gradient
  Descent loop (20 iterations, `learning_rate=0.1`) starting at
  `(10, 10)` — converges to `(0.115, 0.115)`, close to the true minimum
  at the origin, with `f(x,y)` decaying from 200 down to ~0.027.
- Sigmoid activation function and its derivative, verified numerically
  the same way as the earlier sections.

Every derivative in this file is checked two ways (symbolic formula vs.
numerical approximation) rather than taken on faith — this is the same
sanity check used in practice to confirm a hand-derived gradient is
correct before trusting it in training code.

### Output
Console output only (no plots/files).

---

# Statistics

## Industry context
Random variables, conditional probability, Bayes' theorem, and
distributions are essential across ML: Naive Bayes classifiers, hidden
Markov models, and the probabilistic reasoning inside transformer models
(token likelihoods) all lean on this foundation. Hypothesis testing,
p-values, and confidence intervals are used throughout ML engineering to
evaluate models and production systems — comparing Model A vs. Model B,
or interpreting an A/B test — which is why it was added here even though
it wasn't in the original roadmap image.

## Core concepts

**Central tendency and spread**
- Mean — the average; pulled hard by outliers since it uses every value.
- Median — the middle value after sorting; robust to outliers because
  it only depends on position, not magnitude.
- Standard deviation — how spread out the data is around the mean.
  Feature scaling (`StandardScaler`) is literally
  `(x - mean) / std` applied per feature before training.

**Normal distribution**
Bell-curve shape, symmetric around the mean. Extremely common in
real-world data (heights, measurement error) and used constantly in ML
for weight initialization and noise assumptions.
- **68-95-99.7 rule**: ~68% of data falls within `mean ± 1 std`, ~95%
  within `mean ± 2 std`, ~99.7% within `mean ± 3 std`. Verified with
  boolean masking — `True`/`False` comparisons are treated as `1`/`0`
  by NumPy, so `np.mean(condition) * 100` directly gives the percentage
  satisfying that condition.

**Binomial distribution**
The outcome of a fixed number of independent yes/no trials (e.g. "how
many heads in 10 coin flips"). Expected value = `n * p`. The
experimental mean from repeated random trials converges toward this
theoretical value as sample size grows — an informal demonstration of
the **Law of Large Numbers**.

**Bayes' Theorem**
```
P(A|B) = P(B|A) * P(A) / P(B)
```

- `P(A)` — prior (belief before new evidence)
- `P(B|A)` — likelihood (how likely the evidence is, given A)
- `P(A|B)` — posterior (updated belief after evidence)

Powers the Naive Bayes classifier (spam detection) and shows up in
model calibration and missing-data imputation. The classic medical-test
example demonstrates the **base-rate effect**: even a 95%-accurate test
gives a surprisingly low probability of actually having a rare disease
after a positive result, because the disease's low prior probability
dominates. Working it out with concrete counts (100 diseased vs. 9,900
healthy out of 10,000 people) makes the ~8.76% result intuitive instead
of just algebraic — this "natural frequencies" framing is a standard
way to teach Bayes' theorem without it feeling like a trick.

**Correlation**
Measures the strength and direction of a *linear* relationship between
two variables, from -1 to +1. `np.corrcoef()` returns a 2x2 matrix;
the off-diagonal value is the coefficient. Important caveat: correlation
is not causation — two variables can move together without one causing
the other, often because both are driven by a third factor.

**Hypothesis testing**
Used to decide whether an observed difference (e.g. Model A vs. Model B
accuracy) reflects a real effect or could plausibly be random noise.
- `H0` (null hypothesis) — assumed true by default: "no real difference."
- `H1` (alternative hypothesis) — "there is a real difference."
- **p-value** — the probability of seeing a result this extreme (or
  more) *if H0 were actually true*. A small p-value means the observed
  result would be unlikely under "no real difference," which is
  evidence against H0.
- **alpha (0.05)** — the significance threshold. `p < alpha` → reject
  H0 (statistically significant); `p >= alpha` → fail to reject H0
  (not enough evidence).
- `scipy.stats.ttest_ind()` — independent two-sample t-test; compares
  the means of two groups and returns a t-statistic and p-value.
- Important caveat, both directions: rejecting H0 does not "prove"
  Model B is better, and failing to reject H0 does not "prove" the
  models are identical — it only reflects the strength of evidence at
  the chosen threshold.

## Tasks
- `01_central_tendency_spread.py` — mean/median/std on a dataset with a
  deliberate outlier; shows the mean shifting sharply while the median
  stays stable.
- `02_normal_distribution.py` — generates normal data and empirically
  verifies the 68-95-99.7 rule via boolean masking.
- `03_binomial_distribution.py` — simulates 1000 experiments of 10 coin
  flips; compares experimental mean to the theoretical `n*p`.
- `04_bayes_medical_test.py` — rare-disease/positive-test scenario;
  computes `P(disease|positive)` via Bayes' theorem and cross-checks it
  against a manual natural-frequencies calculation.
- `05_correlation.py` — compares an engineered relationship (`y` built
  from `x` plus noise) against an unrelated variable (`z`), showing
  strong vs. near-zero correlation, with a note on correlation ≠
  causation.
- `06_hypothesis_testing.py` — independent t-test on two scenarios:
  Model A vs. Model B (real generated difference → low p-value →
  reject H0) and Model C vs. Model D (no real difference, same
  underlying distribution → high p-value → fail to reject H0).

### Output
Console output only across all six scripts.