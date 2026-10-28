from speclib import *
TITLE = "MLExpert · Learning to Rank"; OUT = "mlexpert/19_learning_to_rank"; M = "mlexpert/mlexpert/learning_to_rank.py"
SLIDES = [
 title("Learning to Rank", "NDCG and a pairwise ranker", "Search engines and feeds don't need exact scores; they need the right order. This lecture covers the NDCG metric and a pairwise, RankNet-style ranker."),
 bullets("The problem", ["Query → many candidate documents", "Order them by relevance", "Top positions matter most"],
  "For each query we have candidate documents with graded relevance. We want to order them so the most relevant appear first, because users rarely look past the top few results."),
 eqs("DCG and NDCG", [r"$DCG@k=\sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}$", r"$NDCG=\frac{DCG}{IDCG}$"], ["Gain grows with relevance", "Discount shrinks with position", "Normalise by the ideal order → [0, 1]"],
  "DCG rewards relevant documents, with gains that grow exponentially in relevance, and discounts them by the log of their position. Dividing by the DCG of the ideal ordering gives NDCG, between zero and one."),
 code("NDCG", src(M, "dcg", "ndcg"), "The code is a direct translation: compute gains and log discounts for the first k items, and divide by the DCG of the sorted, ideal list."),
 eqs("Pairwise approach", [r"$L=\sum_{(i,j):\,rel_i>rel_j}\log\left(1+e^{-(s_i-s_j)}\right)$"], ["Turn ranking into 'is i above j?' decisions", "Only compare documents of the same query", "Logistic loss on score differences"],
  "Directly optimising NDCG is hard because sorting isn't differentiable. The pairwise trick: for every pair in the same query where i is more relevant than j, we want i's score higher. A logistic loss on the score difference does that, as in RankNet."),
 code("PairwiseRanker.fit", src(M, "PairwiseRanker.fit"), "The ranker builds all valid pairs within each query, takes feature differences, and runs gradient ascent on the log-likelihood that the more relevant item wins. Scores are a linear model, X times w."),
 bullets("Trade-offs", ["Pointwise: regress relevance — simple, ignores order", "Pairwise: O(m²) pairs per query", "Listwise (LambdaMART): optimise NDCG-like objectives", "Watch position bias in click labels"],
  "There are three families. Pointwise regresses relevance directly but ignores ordering. Pairwise, like ours, learns order but has quadratic pairs per query. Listwise methods like LambdaMART optimise NDCG-style objectives. With click data, always correct for position bias."),
 bullets("Recap", ["Evaluate with NDCG@k", "Pairwise: logistic loss on score differences", "Pairs only within a query", "Listwise methods for production"],
  "To recap: evaluate rankings with NDCG at k, train a pairwise ranker with logistic loss on score differences within each query, and reach for listwise methods in production."),
]
