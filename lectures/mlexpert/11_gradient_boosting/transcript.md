# MLExpert · Gradient Boosting

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Gradient Boosting (0:00) — `slides/01.png`

Gradient boosting is behind XGBoost and LightGBM, the go-to models for tabular data. The idea: add small trees one at a time, each correcting the mistakes of the ensemble so far.

## 2. The problem (0:11) — `slides/02.png`

On tabular data, one tree is either too shallow to capture the pattern or deep enough to overfit. Forests average independent trees. Boosting asks a different question: can each new tree specifically fix what the previous ones got wrong?

## 3. Intuition: fit the residuals (0:27) — `slides/03.png`

Start with the mean as the prediction. Compute residuals, what's left to explain, and fit a small tree to them. Add that tree, scaled by a learning rate. Repeat. For squared loss, the residual is exactly the negative gradient, so this is gradient descent in function space.

## 4. The boosting loop (0:46) — `slides/04.png`

The code is short. Initialise with the mean. Each round, fit a depth-limited regression tree to y minus the current prediction, add its shrunken output, and record the training loss, which should fall steadily.

## 5. Regression trees with prefix sums (0:59) — `slides/05.png`

The base learner is a regression tree whose leaves predict means. To find splits fast, we sort each feature and use cumulative sums of y and y squared, so every candidate split's squared error is computed in constant time.

## 6. Fast split search (1:12) — `slides/06.png`

Here's that scan. For each feature we sort, build the prefix sums, skip positions where neighbouring values are equal, and compute left plus right squared error in constant time per split.

## 7. Complexity & trade-offs (1:24) — `slides/07.png`

Training costs the number of trees times d times n log n, and it's sequential, unlike forests. You tune the learning rate, number of trees, and depth together, ideally with early stopping on validation loss. When tuned, it usually beats random forests on tabular data.

## 8. Recap (1:41) — `slides/08.png`

To recap: start from the mean, fit each new tree to the residuals, shrink it with a learning rate, and repeat. It's gradient descent where each step is a tree.
