Xb = np.hstack([X, np.ones((n, 1))])        # add bias column
reg = self.l2 * np.eye(d + 1)
reg[-1, -1] = 0                             # don't regularise bias
theta = np.linalg.solve(Xb.T @ Xb + reg, Xb.T @ y)
self.w, self.b = theta[:-1], theta[-1]
