"""Gaussian Naive Bayes classifier."""
import numpy as np


class GaussianNB:
    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y)
        self.classes_ = np.unique(y)
        self.mu = np.array([X[y == c].mean(0) for c in self.classes_])
        self.var = np.array([X[y == c].var(0) + 1e-9 for c in self.classes_])
        self.logprior = np.log(np.array([np.mean(y == c) for c in self.classes_]))
        return self

    def predict_log_proba_unnormalized(self, X):
        X = np.asarray(X, float)
        ll = -0.5 * (np.log(2 * np.pi * self.var)[None] + (X[:, None, :] - self.mu[None]) ** 2 / self.var[None]).sum(-1)
        return ll + self.logprior

    def predict(self, X):
        return self.classes_[np.argmax(self.predict_log_proba_unnormalized(X), axis=1)]
