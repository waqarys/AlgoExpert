def one_hot(y, n_classes=None):
    y = np.asarray(y, int)
    n = n_classes or y.max() + 1
    out = np.zeros((len(y), n))
    out[np.arange(len(y)), y] = 1
    return out
