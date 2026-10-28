"""Linear regression via closed form (normal equation) or gradient descent, with optional L2 (ridge)."""
import numpy as np


class LinearRegression:
    def __init__(self, method="closed_form", lr=0.01, epochs=1000, l2=0.0):
        self.method, self.lr, self.epochs, self.l2 = method, lr, epochs, l2
        self.w, self.b = None, 0.0

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y, float)
        n, d = X.shape
        if self.method == "closed_form":
            Xb = np.hstack([X, np.ones((n, 1))])
            reg = self.l2 * np.eye(d + 1)
            reg[-1, -1] = 0  # don't regularise bias
            theta = np.linalg.solve(Xb.T @ Xb + reg, Xb.T @ y)
            self.w, self.b = theta[:-1], theta[-1]
        else:
            self.w, self.b = np.zeros(d), 0.0
            for _ in range(self.epochs):
                err = X @ self.w + self.b - y
                self.w -= self.lr * (2 * X.T @ err / n + 2 * self.l2 * self.w)
                self.b -= self.lr * 2 * err.mean()
        return self

    def predict(self, X):
        return np.asarray(X, float) @ self.w + self.b
