"""k-nearest neighbours classifier and regressor (Euclidean distance)."""
import numpy as np


class KNN:
    def __init__(self, k=3, task="classification"):
        self.k, self.task = k, task

    def fit(self, X, y):
        self.X, self.y = np.asarray(X, float), np.asarray(y)
        return self

    def predict(self, X):
        X = np.asarray(X, float)
        d = ((X[:, None, :] - self.X[None, :, :]) ** 2).sum(-1)
        nn = np.argsort(d, axis=1)[:, :self.k]
        labels = self.y[nn]
        if self.task == "regression":
            return labels.mean(axis=1)
        out = []
        for row in labels:
            vals, counts = np.unique(row, return_counts=True)
            out.append(vals[np.argmax(counts)])
        return np.array(out)
