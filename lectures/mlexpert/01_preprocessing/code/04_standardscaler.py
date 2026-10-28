class StandardScaler:
    def fit(self, X):
        X = np.asarray(X, float)
        self.mean_, self.std_ = X.mean(0), X.std(0)
        self.std_[self.std_ == 0] = 1
        return self

    def transform(self, X):
        return (np.asarray(X, float) - self.mean_) / self.std_
