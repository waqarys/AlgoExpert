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
