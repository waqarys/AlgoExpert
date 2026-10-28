"""Gradient descent variants operating on a gradient function grad(w, X, y)."""
import numpy as np


def batch_gd(grad, w0, X, y, lr=0.1, epochs=100):
    w = np.array(w0, float)
    for _ in range(epochs):
        w -= lr * grad(w, X, y)
    return w


def minibatch_sgd(grad, w0, X, y, lr=0.1, epochs=50, batch_size=16, seed=0):
    rng = np.random.default_rng(seed)
    w = np.array(w0, float)
    n = len(X)
    for _ in range(epochs):
        idx = rng.permutation(n)
        for s in range(0, n, batch_size):
            b = idx[s:s + batch_size]
            w -= lr * grad(w, X[b], y[b])
    return w


def momentum_gd(grad, w0, X, y, lr=0.1, beta=0.9, epochs=100):
    w, v = np.array(w0, float), np.zeros_like(w0, dtype=float)
    for _ in range(epochs):
        v = beta * v + grad(w, X, y)
        w -= lr * v
    return w


def adam(grad, w0, X, y, lr=0.05, b1=0.9, b2=0.999, eps=1e-8, epochs=300):
    w = np.array(w0, float)
    m, v = np.zeros_like(w), np.zeros_like(w)
    for t in range(1, epochs + 1):
        g = grad(w, X, y)
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * g * g
        mh, vh = m / (1 - b1 ** t), v / (1 - b2 ** t)
        w -= lr * mh / (np.sqrt(vh) + eps)
    return w


def mse_grad(w, X, y):
    """Gradient of mean squared error for a linear model with weights w (bias as last column of X)."""
    return 2 * X.T @ (X @ w - y) / len(X)
