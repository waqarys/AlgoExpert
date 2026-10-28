"""k-means clustering with k-means++ initialisation."""
import numpy as np


class KMeans:
    def __init__(self, k, max_iter=100, seed=0, tol=1e-6):
        self.k, self.max_iter, self.seed, self.tol = k, max_iter, seed, tol

    def _init(self, X, rng):
        centers = [X[rng.integers(len(X))]]
        for _ in range(1, self.k):
            d2 = np.min(((X[:, None] - np.array(centers)[None]) ** 2).sum(-1), axis=1)
            centers.append(X[rng.choice(len(X), p=d2 / d2.sum())])
        return np.array(centers)

    def fit(self, X):
        X = np.asarray(X, float)
        rng = np.random.default_rng(self.seed)
        self.centers = self._init(X, rng)
        for _ in range(self.max_iter):
            labels = self.predict(X)
            new = np.array([X[labels == j].mean(0) if np.any(labels == j) else self.centers[j] for j in range(self.k)])
            shift = np.abs(new - self.centers).max()
            self.centers = new
            if shift < self.tol:
                break
        self.labels_ = self.predict(X)
        self.inertia_ = float(((X - self.centers[self.labels_]) ** 2).sum())
        return self

    def predict(self, X):
        X = np.asarray(X, float)
        return np.argmin(((X[:, None] - self.centers[None]) ** 2).sum(-1), axis=1)
