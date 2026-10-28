def fit(self, X, y):
    X, y = np.asarray(X, float), np.asarray(y)
    for _ in range(self.epochs):
        idx = self.rng.permutation(len(X))
        for s in range(0, len(X), self.batch_size):
            bi = idx[s:s + self.batch_size]
            gW, gb = self.gradients(X[bi], y[bi])
            for i in range(len(self.W)):
                self.W[i] -= self.lr * gW[i]
                self.b[i] -= self.lr * gb[i]
    return self
