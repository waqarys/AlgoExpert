def roc_auc(y_true, scores):
    """AUC = probability a random positive scores above a random negative (ties count half)."""
    y_true, scores = np.asarray(y_true), np.asarray(scores, dtype=float)
    pos, neg = scores[y_true == 1], scores[y_true == 0]
    if len(pos) == 0 or len(neg) == 0:
        raise ValueError("need both classes")
    diff = pos[:, None] - neg[None, :]
    return float(np.mean((diff > 0) + 0.5 * (diff == 0)))
