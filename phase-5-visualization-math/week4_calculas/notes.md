# Week 3-4 — Calculus

## Industry context
Entry-level ML math needs calculus (derivatives, chain rule) enough to
understand backpropagation conceptually, not a graduate-level treatment.
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

## Output
Console output only (no plots/files) — this topic is about verifying
mathematical relationships numerically, not visualization.