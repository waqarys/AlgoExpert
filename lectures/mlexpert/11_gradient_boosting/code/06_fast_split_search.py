for j in range(X.shape[1]):
    order = np.argsort(X[:, j])
    xs, ys = X[order, j], y[order]
    cs, cs2, n = np.cumsum(ys), np.cumsum(ys ** 2), len(ys)
    for i in range(self.min_leaf, n - self.min_leaf + 1):
        if i == n or xs[i - 1] == xs[i]:  # need a real gap between left and right
            continue
        l_sse = cs2[i - 1] - cs[i - 1] ** 2 / i
        r_sum, r_sq = cs[-1] - cs[i - 1], cs2[-1] - cs2[i - 1]
        sse = l_sse + r_sq - r_sum ** 2 / (n - i)
        if best is None or sse < best[0]:
            best = (sse, j, (xs[i - 1] + xs[i]) / 2)
