def fit(self, X, y):
    X, y = np.asarray(X, float), np.asarray(y, float)
    xm, ym = X.mean(0), y.mean()
    Xc = X - xm
    self.w = np.linalg.solve(Xc.T @ Xc + self.alpha * np.eye(X.shape[1]), Xc.T @ (y - ym))
    self.b = ym - xm @ self.w
    return self
