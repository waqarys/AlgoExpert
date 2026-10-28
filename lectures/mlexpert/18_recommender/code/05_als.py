def fit(self, R, mask=None):
    R = np.asarray(R, float)
    M = ~np.isnan(R) if mask is None else np.asarray(mask, bool)
    R = np.nan_to_num(R)
    rng = np.random.default_rng(self.seed)
    n, m = R.shape
    P, Q = rng.normal(0, 0.1, (n, self.k)), rng.normal(0, 0.1, (m, self.k))
    I = self.reg * np.eye(self.k)
    for _ in range(self.iters):
        for u in range(n):
            Qo = Q[M[u]]
            P[u] = np.linalg.solve(Qo.T @ Qo + I, Qo.T @ R[u, M[u]])
        for i in range(m):
            Po = P[M[:, i]]
            Q[i] = np.linalg.solve(Po.T @ Po + I, Po.T @ R[M[:, i], i])
    self.P, self.Q = P, Q
    return self
