from speclib import *
TITLE = "MLExpert · Multinomial Naive Bayes"; OUT = "mlexpert/09_multinomial_nb"; M = "mlexpert/mlexpert/multinomial_nb.py"
SLIDES = [
 title("Multinomial Naive Bayes", "Text classification with word counts", "Multinomial naive Bayes is the classic text classifier, behind early spam filters. We'll cover the model and two key optimisations: Laplace smoothing and log-space scoring."),
 bullets("The problem", ["Input: word counts per document", "Output: class, e.g. spam / ham", "Vocabulary is large and sparse"],
  "Each document is a vector of word counts over a large vocabulary, mostly zeros. We want to predict its class, like spam or not spam."),
 eqs("Model", [r"$\log P(c\mid x)=\log P(c)+\sum_w x_w\log\theta_{cw}+\mathrm{const}$"], ["θ_cw = share of class c's words that are w", "Score is linear in the counts"],
  "Each class has a distribution over words, theta. A document's log score is the log prior plus, for each word, its count times the log probability of that word in the class. Notice that's just a dot product, a linear model in disguise."),
 eqs("Laplace smoothing", [r"$\theta_{cw}=\frac{N_{cw}+\alpha}{\sum_{w'}N_{cw'}+\alpha V}$"], ["Unseen word → probability 0 → log = −∞", "Add α (usually 1) to every count"],
  "Problem: a word never seen in spam during training gets probability zero, and one zero wipes out the whole product. Laplace smoothing adds alpha to every count, so nothing is ever impossible."),
 code("MultinomialNB", src(M, "MultinomialNB"), "The code sums counts per class, adds alpha, normalises, and takes logs. Prediction is one matrix multiply of counts by log-likelihoods plus the log prior, then argmax. Working in log space avoids underflow on long documents."),
 bullets("Complexity & trade-offs", ["Train O(nnz) — one pass over counts", "Predict: one sparse matrix product", "Ignores word order and correlation", "Great for spam, topics, sentiment baselines"],
  "Training is a single pass over the non-zero counts and prediction is one sparse matrix product, so it scales to huge corpora. It ignores word order and correlations, but it's a remarkably strong baseline for spam, topic, and sentiment classification."),
 bullets("Recap", ["Per-class word distributions", "Laplace smoothing prevents zero probabilities", "Log-space scores = linear model", "Fast and strong for text"],
  "To recap: learn a word distribution per class, smooth with Laplace, score in log space, which turns out to be a linear model, and enjoy a fast, strong text classifier."),
]
