def bias_variance(make_model, f, degree, n_train=30, n_sets=200, noise=0.3, seed=0):
    """Train on n_sets noisy samples of f, evaluate on a fixed grid.
    Returns (bias^2, variance, noise^2) averaged over the grid."""
    rng = np.random.default_rng(seed)
    grid = np.linspace(0, 1, 50)
    Xg = polynomial_features(grid, degree)
    preds = np.empty((n_sets, grid.size))
    for s in range(n_sets):
        x = rng.uniform(0, 1, n_train)
        y = f(x) + rng.normal(0, noise, n_train)
        preds[s] = make_model().fit(polynomial_features(x, degree), y).predict(Xg)
    mean = preds.mean(0)
    return float(np.mean((mean - f(grid)) ** 2)), float(np.mean(preds.var(0))), noise ** 2
