def truncated_svd(A, k, iters=500, seed=0):
    A = np.asarray(A, float)
    rng = np.random.default_rng(seed)
    U, S, V = [], [], []
    R = A.copy()
    for _ in range(k):
        v = rng.normal(size=A.shape[1])
        v /= np.linalg.norm(v)
        for _ in range(iters):
            v = R.T @ (R @ v)
            nv = np.linalg.norm(v)
            if nv == 0:
                break
            v /= nv
        s = np.linalg.norm(R @ v)
        u = R @ v / s if s > 0 else np.zeros(A.shape[0])
        U.append(u); S.append(s); V.append(v)
        R = R - s * np.outer(u, v)
    return np.array(U).T, np.array(S), np.array(V)
