def gini(y):
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return 1 - np.sum(p * p)

# inside DecisionTree._grow
for f in feats:
    for t in np.unique(X[:, f])[:-1]:
        left = X[:, f] <= t
        g = (left.sum() * gini(y[left])
             + (~left).sum() * gini(y[~left])) / len(y)
        if best is None or g < best[0]:
            best = (g, f, t)
