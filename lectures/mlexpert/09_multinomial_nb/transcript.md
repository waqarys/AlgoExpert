# MLExpert · Multinomial Naive Bayes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Multinomial Naive Bayes (0:00) — `slides/01.png`

Multinomial naive Bayes is the classic text classifier, behind early spam filters. We'll cover the model and two key optimisations: Laplace smoothing and log-space scoring.

## 2. The problem (0:11) — `slides/02.png`

Each document is a vector of word counts over a large vocabulary, mostly zeros. We want to predict its class, like spam or not spam.

## 3. Model (0:20) — `slides/03.png`

Each class has a distribution over words, theta. A document's log score is the log prior plus, for each word, its count times the log probability of that word in the class. Notice that's just a dot product, a linear model in disguise.

## 4. Laplace smoothing (0:36) — `slides/04.png`

Problem: a word never seen in spam during training gets probability zero, and one zero wipes out the whole product. Laplace smoothing adds alpha to every count, so nothing is ever impossible.

## 5. MultinomialNB (0:48) — `slides/05.png`

The code sums counts per class, adds alpha, normalises, and takes logs. Prediction is one matrix multiply of counts by log-likelihoods plus the log prior, then argmax. Working in log space avoids underflow on long documents.

## 6. Complexity & trade-offs (1:03) — `slides/06.png`

Training is a single pass over the non-zero counts and prediction is one sparse matrix product, so it scales to huge corpora. It ignores word order and correlations, but it's a remarkably strong baseline for spam, topic, and sentiment classification.

## 7. Recap (1:18) — `slides/07.png`

To recap: learn a word distribution per class, smooth with Laplace, score in log space, which turns out to be a linear model, and enjoy a fast, strong text classifier.
