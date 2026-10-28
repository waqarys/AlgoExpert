def fit(self, X, y):
    X, y = np.asarray(X, float), np.asarray(y, float)
    n, d = X.shape
    self.w, self.b = np.zeros(d), 0.0
    for _ in range(self.epochs):
        p = sigmoid(X @ self.w + self.b)
        self.w -= self.lr * (X.T @ (p - y) / n + self.l2 * self.w)
        self.b -= self.lr * np.mean(p - y)
    return self
