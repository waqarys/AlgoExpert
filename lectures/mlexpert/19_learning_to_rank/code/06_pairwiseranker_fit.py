def fit(self, X, rel, qid):
    X, rel, qid = np.asarray(X, float), np.asarray(rel), np.asarray(qid)
    pairs = [(i, j) for q in np.unique(qid) for i in np.where(qid == q)[0] for j in np.where(qid == q)[0] if rel[i] > rel[j]]
    self.w = np.zeros(X.shape[1])
    if not pairs:
        return self
    I, J = np.array(pairs).T
    D = X[I] - X[J]
    for _ in range(self.epochs):
        p = 1 / (1 + np.exp(D @ self.w))  # = sigmoid(-(s_i - s_j))
        self.w += self.lr * (D * p[:, None]).mean(0)
    return self
