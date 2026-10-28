# MLExpert · Gaussian Naive Bayes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Naive Bayes (0:00) — `slides/01.png`

Naive Bayes is a probabilistic classifier built on Bayes' rule and one bold simplification. It trains in a single pass and is surprisingly strong. Let's build the Gaussian version.

## 2. The problem (0:12) — `slides/02.png`

We want to classify by asking which class is most probable given the features, and we want it fast, even with little data and many features.

## 3. Bayes' rule + the naive assumption (0:20) — `slides/03.png`

Bayes' rule says the class probability is proportional to the prior times the likelihood. The naive part assumes features are independent given the class, so the likelihood becomes a product of one-dimensional terms, each trivial to estimate.

## 4. Gaussian likelihood in log space (0:34) — `slides/04.png`

For continuous features we model each one as a Gaussian per class, with its own mean and variance. Multiplying many small probabilities underflows, so we add logs instead. A tiny epsilon on the variance avoids division by zero.

## 5. GaussianNB (0:49) — `slides/05.png`

Fitting computes per-class means, variances, and log priors, in one pass. Prediction evaluates the log-likelihood for every class with broadcasting, adds the log prior, and takes the argmax.

## 6. Complexity & trade-offs (1:02) — `slides/06.png`

Training is one pass over the data, and prediction is linear in classes times features. It works with very little data and has nothing to tune. Its independence assumption is rarely true, so probabilities are over-confident, but the ranking of classes is often still right.

## 7. Recap (1:19) — `slides/07.png`

To recap: posterior is proportional to prior times a product of per-feature likelihoods, each a Gaussian here. Work in log space. It's a fast, strong baseline. Next we'll see the word-count version used for text.
