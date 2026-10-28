"""Binary logistic regression trained with gradient descent on cross-entropy loss."""
import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))


class LogisticRegression:
    def __init__(self, lr=0.1, epochs=2000, l2=0.0):
        self.lr, self.epochs, self.l2 = lr, epochs, l2

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y, float)
        n, d = X.shape
        self.w, self.b = np.zeros(d), 0.0
        for _ in range(self.epochs):
            p = sigmoid(X @ self.w + self.b)
            self.w -= self.lr * (X.T @ (p - y) / n + self.l2 * self.w)
            self.b -= self.lr * np.mean(p - y)
        return self

    def predict_proba(self, X):
        return sigmoid(np.asarray(X, float) @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)


def softmax(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


class SoftmaxRegression:
    """Multinomial logistic regression."""

    def __init__(self, lr=0.1, epochs=2000):
        self.lr, self.epochs = lr, epochs

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y)
        self.classes_ = np.unique(y)
        Y = (y[:, None] == self.classes_[None, :]).astype(float)
        n, d = X.shape
        self.W, self.b = np.zeros((d, len(self.classes_))), np.zeros(len(self.classes_))
        for _ in range(self.epochs):
            P = softmax(X @ self.W + self.b)
            self.W -= self.lr * X.T @ (P - Y) / n
            self.b -= self.lr * (P - Y).mean(axis=0)
        return self

    def predict(self, X):
        return self.classes_[np.argmax(np.asarray(X, float) @ self.W + self.b, axis=1)]
