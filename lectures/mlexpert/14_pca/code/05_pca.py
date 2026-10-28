class PCA:
    def __init__(self, n_components):
        self.n_components = n_components

    def fit(self, X):
        X = np.asarray(X, float)
        self.mean_ = X.mean(0)
        _, s, vt = np.linalg.svd(X - self.mean_, full_matrices=False)
        self.components_ = vt[:self.n_components]
        var = s ** 2 / (len(X) - 1)
        self.explained_variance_ratio_ = var[:self.n_components] / var.sum()
        return self

    def transform(self, X):
        return (np.asarray(X, float) - self.mean_) @ self.components_.T

    def inverse_transform(self, Z):
        return Z @ self.components_ + self.mean_
