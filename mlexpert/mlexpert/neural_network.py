"""Fully connected neural network (ReLU hidden layers, softmax output) trained with backprop + mini-batch SGD."""
import numpy as np


class MLP:
    def __init__(self, sizes, lr=0.1, epochs=500, batch_size=32, seed=0):
        rng = np.random.default_rng(seed)
        self.W = [rng.normal(0, np.sqrt(2 / a), (a, b)) for a, b in zip(sizes[:-1], sizes[1:])]
        self.b = [np.zeros(b) for b in sizes[1:]]
        self.lr, self.epochs, self.batch_size, self.rng = lr, epochs, batch_size, rng

    def _forward(self, X):
        acts = [X]
        for i, (W, b) in enumerate(zip(self.W, self.b)):
            z = acts[-1] @ W + b
            if i < len(self.W) - 1:
                acts.append(np.maximum(z, 0))
            else:
                z = z - z.max(1, keepdims=True)
                e = np.exp(z)
                acts.append(e / e.sum(1, keepdims=True))
        return acts

    def loss(self, X, y):
        p = self._forward(np.asarray(X, float))[-1]
        return float(-np.mean(np.log(p[np.arange(len(y)), y] + 1e-12)))

    def gradients(self, X, y):
        acts = self._forward(X)
        delta = acts[-1].copy()
        delta[np.arange(len(y)), y] -= 1
        delta /= len(y)
        gW, gb = [None] * len(self.W), [None] * len(self.b)
        for i in reversed(range(len(self.W))):
            gW[i] = acts[i].T @ delta
            gb[i] = delta.sum(0)
            if i > 0:
                delta = (delta @ self.W[i].T) * (acts[i] > 0)
        return gW, gb

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y)
        for _ in range(self.epochs):
            idx = self.rng.permutation(len(X))
            for s in range(0, len(X), self.batch_size):
                bi = idx[s:s + self.batch_size]
                gW, gb = self.gradients(X[bi], y[bi])
                for i in range(len(self.W)):
                    self.W[i] -= self.lr * gW[i]
                    self.b[i] -= self.lr * gb[i]
        return self

    def predict(self, X):
        return np.argmax(self._forward(np.asarray(X, float))[-1], axis=1)
