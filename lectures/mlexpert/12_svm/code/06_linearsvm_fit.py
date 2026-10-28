def fit(self, X, y):
    X = np.asarray(X, float)
    y = np.where(np.asarray(y) > 0, 1.0, -1.0)
    self.classes_ = (0, 1)
    Xb = np.hstack([X, np.ones((len(X), 1))])  # bias as extra feature
    w = np.zeros(Xb.shape[1])
    rng, t = np.random.default_rng(self.seed), 0
    for _ in range(self.epochs):
        for i in rng.permutation(len(X)):
            t += 1
            eta = 1.0 / (self.lam * t)
            margin = y[i] * Xb[i] @ w
            w *= 1 - eta * self.lam
            if margin < 1:
                w += eta * y[i] * Xb[i]
    self.w, self.b = w[:-1], w[-1]
    return self
