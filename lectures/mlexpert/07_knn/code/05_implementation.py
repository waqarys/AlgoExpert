def predict(self, X):
    X = np.asarray(X, float)
    d = ((X[:, None, :] - self.X[None, :, :]) ** 2).sum(-1)
    nn = np.argsort(d, axis=1)[:, :self.k]
    labels = self.y[nn]
    if self.task == "regression":
        return labels.mean(axis=1)
    out = []
    for row in labels:
        vals, counts = np.unique(row, return_counts=True)
        out.append(vals[np.argmax(counts)])
    return np.array(out)
