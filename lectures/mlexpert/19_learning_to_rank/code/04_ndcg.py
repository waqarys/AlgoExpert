def dcg(rels, k=None):
    rels = np.asarray(rels, float)[:k]
    return float(np.sum((2 ** rels - 1) / np.log2(np.arange(2, rels.size + 2))))

def ndcg(rels_in_ranked_order, k=None):
    ideal = dcg(sorted(rels_in_ranked_order, reverse=True), k)
    return dcg(rels_in_ranked_order, k) / ideal if ideal > 0 else 0.0
