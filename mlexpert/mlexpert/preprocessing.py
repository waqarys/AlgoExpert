"""Common preprocessing utilities: scaling, one-hot encoding, train/test split, k-fold indices."""
import numpy as np


class StandardScaler:
    def fit(self, X):
        X = np.asarray(X, float)
        self.mean_, self.std_ = X.mean(0), X.std(0)
        self.std_[self.std_ == 0] = 1
        return self

    def transform(self, X):
        return (np.asarray(X, float) - self.mean_) / self.std_


def one_hot(y, n_classes=None):
    y = np.asarray(y, int)
    n = n_classes or y.max() + 1
    out = np.zeros((len(y), n))
    out[np.arange(len(y)), y] = 1
    return out


def train_test_split(X, y, test_size=0.25, seed=0):
    idx = np.random.default_rng(seed).permutation(len(X))
    cut = int(len(X) * (1 - test_size))
    return X[idx[:cut]], X[idx[cut:]], y[idx[:cut]], y[idx[cut:]]


def k_fold_indices(n, k, seed=0):
    idx = np.random.default_rng(seed).permutation(n)
    folds = np.array_split(idx, k)
    return [(np.concatenate(folds[:i] + folds[i + 1:]), folds[i]) for i in range(k)]
