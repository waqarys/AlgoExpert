def fit(self, X, y):
    X, y = np.asarray(X, float), np.asarray(y)
    rng = np.random.default_rng(self.seed)
    mf = self.max_features or max(1, int(np.sqrt(X.shape[1])))
    self.trees = []
    for i in range(self.n_trees):
        idx = rng.integers(0, len(X), len(X))
        self.trees.append(DecisionTree(self.max_depth, max_features=mf, seed=self.seed + i).fit(X[idx], y[idx]))
    return self
