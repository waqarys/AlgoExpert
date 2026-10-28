def batch_gd(grad, w0, X, y, lr=0.1, epochs=100):
    w = np.array(w0, float)
    for _ in range(epochs):
        w -= lr * grad(w, X, y)
    return w

def minibatch_sgd(grad, w0, X, y, lr=0.1, epochs=50, batch_size=16, seed=0):
    rng = np.random.default_rng(seed)
    w = np.array(w0, float)
    n = len(X)
    for _ in range(epochs):
        idx = rng.permutation(n)
        for s in range(0, n, batch_size):
            b = idx[s:s + batch_size]
            w -= lr * grad(w, X[b], y[b])
    return w
