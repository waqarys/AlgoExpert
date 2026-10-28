from speclib import *
TITLE = "MLExpert · Gaussian Naive Bayes"; OUT = "mlexpert/08_naive_bayes"; M = "mlexpert/mlexpert/naive_bayes.py"
SLIDES = [
 title("Naive Bayes", "Gaussian Naive Bayes from scratch", "Naive Bayes is a probabilistic classifier built on Bayes' rule and one bold simplification. It trains in a single pass and is surprisingly strong. Let's build the Gaussian version."),
 bullets("The problem", ["Classify using probabilities", "Few training examples, many features", "Need something fast and simple"],
  "We want to classify by asking which class is most probable given the features, and we want it fast, even with little data and many features."),
 eqs("Bayes' rule + the naive assumption", [r"$P(c\mid x)\propto P(c)\prod_j P(x_j\mid c)$"], ["Assume features independent given the class", "Then each feature gets its own simple model"],
  "Bayes' rule says the class probability is proportional to the prior times the likelihood. The naive part assumes features are independent given the class, so the likelihood becomes a product of one-dimensional terms, each trivial to estimate."),
 eqs("Gaussian likelihood in log space", [r"$\log P(x_j\mid c)=-\frac{1}{2}\left[\log 2\pi\sigma_{cj}^2+\frac{(x_j-\mu_{cj})^2}{\sigma_{cj}^2}\right]$"], ["Products of tiny numbers underflow → sum logs", "Add a tiny ε to variances"],
  "For continuous features we model each one as a Gaussian per class, with its own mean and variance. Multiplying many small probabilities underflows, so we add logs instead. A tiny epsilon on the variance avoids division by zero."),
 code("GaussianNB", src(M, "GaussianNB"), "Fitting computes per-class means, variances, and log priors, in one pass. Prediction evaluates the log-likelihood for every class with broadcasting, adds the log prior, and takes the argmax."),
 bullets("Complexity & trade-offs", ["Train O(n·d), predict O(c·d)", "Works with tiny datasets; no tuning", "Independence rarely true → probabilities poorly calibrated", "Ranking of classes is often still good"],
  "Training is one pass over the data, and prediction is linear in classes times features. It works with very little data and has nothing to tune. Its independence assumption is rarely true, so probabilities are over-confident, but the ranking of classes is often still right."),
 bullets("Recap", ["Posterior ∝ prior × product of likelihoods", "Gaussian per feature per class", "Work in log space", "Fast, strong baseline"],
  "To recap: posterior is proportional to prior times a product of per-feature likelihoods, each a Gaussian here. Work in log space. It's a fast, strong baseline. Next we'll see the word-count version used for text."),
]
