import numpy as np


# ============================================================
# 1. Basic Derivative — Symbolic / Manual
# ============================================================

def f(x):
    return x**2


def f_derivative(x):
    # Why: By the power rule, d/dx(x^2) = 2x.
    # The derivative tells us the slope of f(x) at a specific x.
    return 2 * x


x = 5

print("=== 1. Basic Derivative ===")
print("Function value f(5):", f(x))
print("Derivative f'(5):", f_derivative(x))
print()


# ============================================================
# 2. Numerical Derivative — Central Difference
# ============================================================

def numerical_derivative(func, x, h=1e-5):
    # Why: Central difference estimates the slope using points
    # on both sides of x. It is generally more accurate than
    # the forward difference formula f(x+h) - f(x).
    return (func(x + h) - func(x - h)) / (2 * h)


symbolic = f_derivative(5)
numerical = numerical_derivative(f, 5)

print("=== 2. Numerical Derivative ===")
print("Symbolic derivative:", symbolic)
print("Numerical derivative:", numerical)
print("Difference:", abs(symbolic - numerical))
print()


# ============================================================
# 3. Chain Rule — Manual Demo
# ============================================================

def g(x):
    return 2 * x + 1


def f_outer(u):
    return u**2


def chain_rule_derivative(x):
    # Why: For a composite function f(g(x)), the chain rule says:
    #
    # d/dx f(g(x)) = f'(g(x)) * g'(x)
    #
    # We first calculate g(x), then evaluate f'(u) at g(x),
    # and finally multiply by g'(x).

    g_x = g(x)

    # Why: The derivative of u^2 is 2u.
    # We evaluate it at u = g(x).
    f_prime_g = 2 * g_x

    # Why: The derivative of 2x + 1 is 2.
    g_prime = 2

    return f_prime_g * g_prime


def composite_function(x):
    # Why: This represents the complete function f(g(x)).
    # g(x) is calculated first, then passed into f_outer().
    return f_outer(g(x))


x = 3

chain_rule_result = chain_rule_derivative(x)
composite_numerical = numerical_derivative(composite_function, x)

print("=== 3. Chain Rule ===")
print("Chain rule derivative at x=3:", chain_rule_result)
print("Numerical derivative at x=3:", composite_numerical)
print("Difference:", abs(chain_rule_result - composite_numerical))
print()


# ============================================================
# 4. Partial Derivatives
# ============================================================

def f_multi(x, y):
    return x**2 + y**2


def partial_x(x, y):
    # Why: When taking the partial derivative with respect to x,
    # y is treated as a constant.
    return 2 * x


def partial_y(x, y):
    # Why: When taking the partial derivative with respect to y,
    # x is treated as a constant.
    return 2 * y


x = 3
y = 4

print("=== 4. Partial Derivatives ===")
print("∂f/∂x at (3,4):", partial_x(x, y))
print("∂f/∂y at (3,4):", partial_y(x, y))
print()


# ============================================================
# 5. Gradient + Gradient Descent
# ============================================================

def gradient(x, y):
    # Why: The gradient combines all partial derivatives into
    # one vector. It tells us the direction of steepest increase.
    return np.array([
        partial_x(x, y),
        partial_y(x, y)
    ])


x = 3
y = 4

print("=== 5. Gradient ===")
print("Gradient at (3,4):", gradient(x, y))
print()


# ------------------------------------------------------------
# Gradient Descent
# ------------------------------------------------------------

x = 10
y = 10

learning_rate = 0.1
iterations = 20

print("=== Gradient Descent ===")

for iteration in range(iterations):
    # Calculate the gradient at the current position.
    grad = gradient(x, y)

    # Why: The gradient points toward the direction of
    # steepest increase. To minimize the function, we move
    # in the opposite direction.
    x = x - learning_rate * grad[0]
    y = y - learning_rate * grad[1]

    print(
        f"Iteration {iteration + 1:2d}: "
        f"x={x:.6f}, y={y:.6f}, "
        f"f(x,y)={f_multi(x, y):.6f}"
    )


print()
print("Final x:", x)
print("Final y:", y)
print("Final f(x,y):", f_multi(x, y))

# ============================================================
# Sigmoid Activation Function — Derivative
# ============================================================

def sigmoid(x):
    # Why: Sigmoid "squashes" any real number into the range (0, 1) —
    # this is what lets a neural network output something interpretable
    # as a probability, and is one of the most common activation
    # functions used between layers.
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    # Why: This is a chain rule result — sigmoid is a composite function
    # (1 / (1 + e^-x)), and differentiating it algebraically simplifies
    # to this remarkably clean form: sigmoid(x) * (1 - sigmoid(x)).
    # This is exactly why sigmoid is convenient to use in backprop —
    # once you've computed sigmoid(x) in the forward pass, you get its
    # derivative almost for free during the backward pass.
    s = sigmoid(x)
    return s * (1 - s)


x = 2

sigmoid_symbolic = sigmoid_derivative(x)
sigmoid_numerical = numerical_derivative(sigmoid, x)

print("=== 6. Sigmoid Derivative ===")
print("sigmoid(2):", sigmoid(x))
print("Symbolic derivative:", sigmoid_symbolic)
print("Numerical derivative:", sigmoid_numerical)
print("Difference:", abs(sigmoid_symbolic - sigmoid_numerical))