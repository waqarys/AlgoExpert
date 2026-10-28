from speclib import *
TITLE = "MLExpert · Recommender Systems"; OUT = "mlexpert/18_recommender"; M = "mlexpert/mlexpert/recommender.py"
SLIDES = [
 title("Recommender Systems", "Collaborative and content-based filtering", "Recommenders decide what you watch, read, and buy. We'll build collaborative filtering with matrix factorisation, and content-based similarity, from scratch."),
 bullets("The problem", ["Users × items rating matrix, mostly empty", "Predict the missing ratings", "Recommend the highest predictions"],
  "We have a users by items matrix of ratings, and almost all of it is missing. The task is to predict the missing entries and recommend each user's top predicted items."),
 eqs("Matrix factorisation", [r"$R\approx PQ^\top,\quad \hat r_{ui}=p_u\cdot q_i$"], ["p_u: user taste vector (k dims)", "q_i: item trait vector (k dims)", "Fit only observed entries"],
  "Collaborative filtering by matrix factorisation gives every user and every item a short vector of k hidden factors. A predicted rating is the dot product of the two. Factors might come to mean things like action versus romance, learned purely from ratings."),
 eqs("Alternating least squares", [r"$p_u=(Q_o^\top Q_o+\lambda I)^{-1}Q_o^\top r_u$"], ["Fix Q → each user is a small ridge regression", "Fix P → each item is a ridge regression", "Alternate until it settles"],
  "Solving for P and Q together is hard, but if we fix the item vectors, each user's vector is just a small ridge regression on the items they rated. Then fix users and solve for items. Alternating between them is ALS, and each step can only lower the loss."),
 code("ALS", src(M, "MatrixFactorization.fit"), "The code builds a mask of observed entries, initialises small random factors, then alternates: for each user, solve a k by k system using only the items they rated, then the same for each item."),
 bullets("Content-based filtering", ["Describe items by features (genre, tags, text)", "Cosine similarity between item vectors", "Recommend items similar to what the user liked", "Solves item cold-start"],
  "Content-based filtering instead describes items by features, like genre or tags, and recommends items similar to what the user already liked, using cosine similarity. It works for brand-new items that have no ratings yet."),
 code("Cosine similarity", src(M, "content_similarity"), "Normalise each item's feature vector to unit length, guarding zero vectors, and one matrix product gives all pairwise cosine similarities."),
 bullets("Trade-offs", ["ALS: O(iters · (n + m) · (k³ + nnz·k))", "CF needs interaction history (cold start)", "Content-based: limited novelty", "Production: hybrid + two-stage retrieval → ranking"],
  "ALS costs a small k by k solve per user and item each iteration, and parallelises well. Collaborative filtering struggles with new users and items; content-based methods lack novelty. Real systems are hybrids, often with a fast retrieval stage followed by a ranking model."),
 bullets("Recap", ["Ratings ≈ user · item factors", "ALS = alternating ridge regressions", "Content similarity for cold start", "Combine both in practice"],
  "To recap: model ratings as user times item factors, fit them with alternating ridge regressions, use content similarity for cold start, and combine both in practice."),
]
