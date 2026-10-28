def gradients(self, X, y):
    acts = self._forward(X)
    delta = acts[-1].copy()
    delta[np.arange(len(y)), y] -= 1
    delta /= len(y)
    gW, gb = [None] * len(self.W), [None] * len(self.b)
    for i in reversed(range(len(self.W))):
        gW[i] = acts[i].T @ delta
        gb[i] = delta.sum(0)
        if i > 0:
            delta = (delta @ self.W[i].T) * (acts[i] > 0)
    return gW, gb
