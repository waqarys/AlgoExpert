"""L1 (lasso, coordinate descent), L2 (ridge, closed form) and elastic net linear regression."""
import numpy as np


def soft_threshold(z, g):
    return np.sign(z) * np.maximum(np.abs(z) - g, 0.0)


class ElasticNet:
    """Minimise 1/(2n)||y - Xw - b||^2 + alpha*(l1_ratio*||w||_1 + (1-l1_ratio)/2*||w||^2)."""

    def __init__(self, alpha=0.1, l1_ratio=0.5, max_iter=1000, tol=1e-6):
        self.alpha, self.l1_ratio, self.max_iter, self.tol = alpha, l1_ratio, max_iter, tol

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y, float)
        xm, ym = X.mean(0), y.mean()
        Xc, yc = X - xm, y - ym
        n, d = X.shape
        w = np.zeros(d)
        col_sq = (Xc ** 2).sum(0) / n
        l1, l2 = self.alpha * self.l1_ratio, self.alpha * (1 - self.l1_ratio)
        for _ in range(self.max_iter):
            w_old = w.copy()
            for j in range(d):
                r = yc - Xc @ w + Xc[:, j] * w[j]
                w[j] = soft_threshold(Xc[:, j] @ r / n, l1) / (col_sq[j] + l2) if col_sq[j] + l2 > 0 else 0.0
            if np.max(np.abs(w - w_old)) < self.tol:
                break
        self.w, self.b = w, ym - xm @ w
        return self

    def predict(self, X):
        return np.asarray(X, float) @ self.w + self.b


class Lasso(ElasticNet):
    def __init__(self, alpha=0.1, **kw):
        super().__init__(alpha=alpha, l1_ratio=1.0, **kw)


class Ridge:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y, float)
        xm, ym = X.mean(0), y.mean()
        Xc = X - xm
        self.w = np.linalg.solve(Xc.T @ Xc + self.alpha * np.eye(X.shape[1]), Xc.T @ (y - ym))
        self.b = ym - xm @ self.w
        return self

    def predict(self, X):
        return np.asarray(X, float) @ self.w + self.b
