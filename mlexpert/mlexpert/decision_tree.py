"""CART decision tree classifier (Gini impurity) and a random forest built from it."""
import numpy as np


def gini(y):
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return 1 - np.sum(p * p)


def entropy(y):
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return float(-np.sum(p * np.log2(p)))


class DecisionTree:
    def __init__(self, max_depth=5, min_samples_split=2, max_features=None, seed=0):
        self.max_depth, self.min_samples_split, self.max_features = max_depth, min_samples_split, max_features
        self.rng = np.random.default_rng(seed)

    def fit(self, X, y):
        self.root = self._grow(np.asarray(X, float), np.asarray(y), 0)
        return self

    def _leaf(self, y):
        vals, counts = np.unique(y, return_counts=True)
        return {"leaf": vals[np.argmax(counts)]}

    def _grow(self, X, y, depth):
        if depth >= self.max_depth or len(y) < self.min_samples_split or len(np.unique(y)) == 1:
            return self._leaf(y)
        feats = range(X.shape[1])
        if self.max_features:
            feats = self.rng.choice(X.shape[1], self.max_features, replace=False)
        best, parent = None, gini(y)
        for f in feats:
            for t in np.unique(X[:, f])[:-1]:
                left = X[:, f] <= t
                g = (left.sum() * gini(y[left]) + (~left).sum() * gini(y[~left])) / len(y)
                if g <= parent + 1e-12 and (best is None or g < best[0]):  # allow zero-gain splits (e.g. XOR)
                    best = (g, f, t)
        if best is None:
            return self._leaf(y)
        _, f, t = best
        left = X[:, f] <= t
        return {"f": f, "t": t, "l": self._grow(X[left], y[left], depth + 1), "r": self._grow(X[~left], y[~left], depth + 1)}

    def _one(self, x, n):
        while "leaf" not in n:
            n = n["l"] if x[n["f"]] <= n["t"] else n["r"]
        return n["leaf"]

    def predict(self, X):
        return np.array([self._one(x, self.root) for x in np.asarray(X, float)])


class RandomForest:
    def __init__(self, n_trees=20, max_depth=5, max_features=None, seed=0):
        self.n_trees, self.max_depth, self.max_features, self.seed = n_trees, max_depth, max_features, seed

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y)
        rng = np.random.default_rng(self.seed)
        mf = self.max_features or max(1, int(np.sqrt(X.shape[1])))
        self.trees = []
        for i in range(self.n_trees):
            idx = rng.integers(0, len(X), len(X))
            self.trees.append(DecisionTree(self.max_depth, max_features=mf, seed=self.seed + i).fit(X[idx], y[idx]))
        return self

    def predict(self, X):
        votes = np.array([t.predict(X) for t in self.trees])
        out = []
        for col in votes.T:
            v, c = np.unique(col, return_counts=True)
            out.append(v[np.argmax(c)])
        return np.array(out)
