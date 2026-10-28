"""Linear SVM trained with the Pegasos sub-gradient method on the hinge loss (labels -1/+1 or 0/1)."""
import numpy as np


class LinearSVM:
    def __init__(self, lam=0.01, epochs=50, seed=0):
        self.lam, self.epochs, self.seed = lam, epochs, seed

    def fit(self, X, y):
        X = np.asarray(X, float)
        y = np.where(np.asarray(y) > 0, 1.0, -1.0)
        self.classes_ = (0, 1)
        Xb = np.hstack([X, np.ones((len(X), 1))])  # bias as extra feature
        w = np.zeros(Xb.shape[1])
        rng, t = np.random.default_rng(self.seed), 0
        for _ in range(self.epochs):
            for i in rng.permutation(len(X)):
                t += 1
                eta = 1.0 / (self.lam * t)
                margin = y[i] * Xb[i] @ w
                w *= 1 - eta * self.lam
                if margin < 1:
                    w += eta * y[i] * Xb[i]
        self.w, self.b = w[:-1], w[-1]
        return self

    def decision_function(self, X):
        return np.asarray(X, float) @ self.w + self.b

    def predict(self, X):
        return (self.decision_function(X) >= 0).astype(int)

    def hinge_loss(self, X, y):
        y = np.where(np.asarray(y) > 0, 1.0, -1.0)
        return float(np.maximum(0, 1 - y * self.decision_function(X)).mean() + self.lam / 2 * self.w @ self.w)
