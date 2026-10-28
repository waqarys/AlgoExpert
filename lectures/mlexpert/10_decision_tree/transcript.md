# MLExpert · Decision Trees and Random Forests

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Decision Trees (0:00) — `slides/01.png`

Decision trees learn a sequence of yes-or-no questions about the features. They're interpretable, handle non-linear boundaries, and become state of the art when combined into forests. Let's build both.

## 2. The problem (0:12) — `slides/02.png`

We want a classifier that captures non-linear interactions, works without feature scaling, and produces rules a person can read, like: if income is above fifty thousand and age is under thirty, approve.

## 3. Intuition: twenty questions (0:24) — `slides/03.png`

A tree is a game of twenty questions. Each internal node tests one feature against a threshold and sends the example left or right. Leaves hold the predicted class, the majority label of the training points that landed there.

## 4. Choosing a split: Gini impurity (0:38) — `slides/04.png`

To pick a question, we measure impurity. Gini is one minus the sum of squared class proportions: zero for a pure node. We try every feature and every threshold, and keep the split whose weighted child impurity is lowest. Then recurse.

## 5. Greedy split search (0:54) — `slides/05.png`

In code, the grow function stops at max depth, at small nodes, or when a node is pure, and returns a majority leaf. Otherwise it scans features and thresholds for the lowest weighted Gini, and recurses on both sides.

## 6. Random forest (1:07) — `slides/06.png`

A single deep tree overfits. A random forest trains many trees, each on a bootstrap sample, and each split only looks at a random subset of about the square root of d features. That de-correlates the trees, and voting across them slashes variance.

## 7. RandomForest.fit (1:23) — `slides/07.png`

The forest code draws bootstrap indices, sets max features to the square root of d by default, and trains independent trees with different seeds. Prediction takes the most common vote per example.

## 8. Complexity & trade-offs (1:35) — `slides/08.png`

Our straightforward split search re-scans the node for each threshold; sorting with prefix counts brings it to n log n per feature. Prediction is just a walk of depth steps. A single tree is interpretable but unstable; a forest is accurate and robust, at the cost of interpretability.

## 9. Recap (1:53) — `slides/09.png`

To recap: trees greedily choose threshold questions that minimise weighted Gini, depth limits control overfitting, and random forests combine bagging with feature subsampling for strong, stable predictions.
