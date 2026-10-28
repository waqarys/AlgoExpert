"""Multinomial naive Bayes for word counts with Laplace smoothing and log-space scoring
(crash-course lessons: Naive Bayes, Naive Bayes Optimizations)."""
import numpy as np


class MultinomialNB:
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
        X, y = np.asarray(X, float), np.asarray(y)
        self.classes_ = np.unique(y)
        counts = np.array([X[y == c].sum(0) for c in self.classes_]) + self.alpha
        self.log_likelihood_ = np.log(counts / counts.sum(1, keepdims=True))
        self.log_prior_ = np.log(np.array([np.mean(y == c) for c in self.classes_]))
        return self

    def predict(self, X):
        scores = np.asarray(X, float) @ self.log_likelihood_.T + self.log_prior_
        return self.classes_[scores.argmax(1)]
