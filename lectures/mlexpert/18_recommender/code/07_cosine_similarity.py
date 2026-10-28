def content_similarity(item_features):
    F = np.asarray(item_features, float)
    norms = np.linalg.norm(F, axis=1, keepdims=True)
    F = F / np.where(norms == 0, 1, norms)
    return F @ F.T
