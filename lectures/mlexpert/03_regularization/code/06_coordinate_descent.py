def soft_threshold(z, g):
    return np.sign(z) * np.maximum(np.abs(z) - g, 0.0)

# inside ElasticNet.fit
for j in range(d):
    r = yc - Xc @ w + Xc[:, j] * w[j]       # partial residual
    w[j] = soft_threshold(Xc[:, j] @ r / n, l1) / (col_sq[j] + l2)
