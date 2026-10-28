def cross_val_score(make_model, X, y, k=5, score=None, seed=0):
    """Fit a fresh model on each of k folds; return the k validation scores.
    make_model() builds an unfitted model; score(y_true, y_pred) defaults to accuracy."""
    X, y = np.asarray(X), np.asarray(y)
    if not 2 <= k <= len(X):
        raise ValueError("k must be between 2 and n_samples")
    score = score or (lambda t, p: float(np.mean(t == p)))
    out = []
    for tr, va in k_fold_indices(len(X), k, seed):
        m = make_model().fit(X[tr], y[tr])
        out.append(score(y[va], m.predict(X[va])))
    return np.array(out)
