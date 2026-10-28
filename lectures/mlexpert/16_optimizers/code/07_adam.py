def adam(grad, w0, X, y, lr=0.05, b1=0.9, b2=0.999, eps=1e-8, epochs=300):
    w = np.array(w0, float)
    m, v = np.zeros_like(w), np.zeros_like(w)
    for t in range(1, epochs + 1):
        g = grad(w, X, y)
        m = b1 * m + (1 - b1) * g
        v = b2 * v + (1 - b2) * g * g
        mh, vh = m / (1 - b1 ** t), v / (1 - b2 ** t)
        w -= lr * mh / (np.sqrt(vh) + eps)
    return w
