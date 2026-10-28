self.w, self.b = np.zeros(d), 0.0
for _ in range(self.epochs):
    err = X @ self.w + self.b - y
    self.w -= self.lr * (2 * X.T @ err / n + 2 * self.l2 * self.w)
    self.b -= self.lr * 2 * err.mean()
