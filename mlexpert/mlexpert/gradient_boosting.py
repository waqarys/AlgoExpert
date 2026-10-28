"""Gradient boosting with depth-limited regression trees (squared loss), from scratch."""
import numpy as np


class RegressionTree:
    def __init__(self, max_depth=3, min_samples_leaf=1):
        self.max_depth, self.min_leaf = max_depth, min_samples_leaf

    def fit(self, X, y):
        self.root = self._grow(np.asarray(X, float), np.asarray(y, float), 0)
        return self

    def _grow(self, X, y, depth):
        if depth == self.max_depth or len(y) < 2 * self.min_leaf or np.all(y == y[0]):
            return float(y.mean())
        best = None
        for j in range(X.shape[1]):
            order = np.argsort(X[:, j])
            xs, ys = X[order, j], y[order]
            cs, cs2, n = np.cumsum(ys), np.cumsum(ys ** 2), len(ys)
            for i in range(self.min_leaf, n - self.min_leaf + 1):
                if i == n or xs[i - 1] == xs[i]:  # need a real gap between left and right
                    continue
                l_sse = cs2[i - 1] - cs[i - 1] ** 2 / i
                r_sum, r_sq = cs[-1] - cs[i - 1], cs2[-1] - cs2[i - 1]
                sse = l_sse + r_sq - r_sum ** 2 / (n - i)
                if best is None or sse < best[0]:
                    best = (sse, j, (xs[i - 1] + xs[i]) / 2)
        if best is None:
            return float(y.mean())
        _, j, thr = best
        m = X[:, j] <= thr
        return (j, thr, self._grow(X[m], y[m], depth + 1), self._grow(X[~m], y[~m], depth + 1))

    def _one(self, x, n):
        while isinstance(n, tuple):
            n = n[2] if x[n[0]] <= n[1] else n[3]
        return n

    def predict(self, X):
        return np.array([self._one(x, self.root) for x in np.asarray(X, float)])


class GradientBoostingRegressor:
    """F0 = mean(y); each stage fits a tree to the residuals (negative gradient of squared loss)."""

    def __init__(self, n_estimators=100, learning_rate=0.1, max_depth=3):
        self.n, self.lr, self.depth = n_estimators, learning_rate, max_depth

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y, float)
        self.f0 = float(y.mean())
        pred = np.full(len(y), self.f0)
        self.trees, self.train_loss_ = [], []
        for _ in range(self.n):
            t = RegressionTree(self.depth).fit(X, y - pred)
            pred += self.lr * t.predict(X)
            self.trees.append(t)
            self.train_loss_.append(float(np.mean((y - pred) ** 2)))
        return self

    def predict(self, X):
        return self.f0 + self.lr * sum(t.predict(X) for t in self.trees) if self.trees else np.full(len(X), self.f0)
