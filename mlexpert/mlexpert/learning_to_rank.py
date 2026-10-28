"""Learning to rank: NDCG metric and a pairwise (RankNet-style) linear ranker."""
import numpy as np


def dcg(rels, k=None):
    rels = np.asarray(rels, float)[:k]
    return float(np.sum((2 ** rels - 1) / np.log2(np.arange(2, rels.size + 2))))


def ndcg(rels_in_ranked_order, k=None):
    ideal = dcg(sorted(rels_in_ranked_order, reverse=True), k)
    return dcg(rels_in_ranked_order, k) / ideal if ideal > 0 else 0.0


class PairwiseRanker:
    """Score s = Xw; minimise log(1 + exp(-(s_i - s_j))) for pairs where rel_i > rel_j in the same query."""

    def __init__(self, lr=0.1, epochs=200):
        self.lr, self.epochs = lr, epochs

    def fit(self, X, rel, qid):
        X, rel, qid = np.asarray(X, float), np.asarray(rel), np.asarray(qid)
        pairs = [(i, j) for q in np.unique(qid) for i in np.where(qid == q)[0] for j in np.where(qid == q)[0] if rel[i] > rel[j]]
        self.w = np.zeros(X.shape[1])
        if not pairs:
            return self
        I, J = np.array(pairs).T
        D = X[I] - X[J]
        for _ in range(self.epochs):
            p = 1 / (1 + np.exp(D @ self.w))  # = sigmoid(-(s_i - s_j))
            self.w += self.lr * (D * p[:, None]).mean(0)
        return self

    def score(self, X):
        return np.asarray(X, float) @ self.w
