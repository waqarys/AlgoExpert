def softmax(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)

def fit(self, X, y):
    X, y = np.asarray(X, float), np.asarray(y)
    self.classes_ = np.unique(y)
    Y = (y[:, None] == self.classes_[None, :]).astype(float)
    n, d = X.shape
    self.W, self.b = np.zeros((d, len(self.classes_))), np.zeros(len(self.classes_))
    for _ in range(self.epochs):
        P = softmax(X @ self.W + self.b)
        self.W -= self.lr * X.T @ (P - Y) / n
        self.b -= self.lr * (P - Y).mean(axis=0)
    return self
