from speclib import *
TITLE = "MLExpert · Decision Trees and Random Forests"; OUT = "mlexpert/10_decision_tree"; M = "mlexpert/mlexpert/decision_tree.py"
SLIDES = [
 title("Decision Trees", "CART and Random Forests", "Decision trees learn a sequence of yes-or-no questions about the features. They're interpretable, handle non-linear boundaries, and become state of the art when combined into forests. Let's build both."),
 bullets("The problem", ["Non-linear boundaries, mixed feature types", "Want rules a human can read", "No feature scaling required"],
  "We want a classifier that captures non-linear interactions, works without feature scaling, and produces rules a person can read, like: if income is above fifty thousand and age is under thirty, approve."),
 diagram("Intuition: twenty questions", [("x₂ ≤ 3.1 ?", "x₁ ≤ 0.5 ?"), ("x₂ ≤ 3.1 ?", "leaf: B"), ("x₁ ≤ 0.5 ?", "leaf: A"), ("x₁ ≤ 0.5 ?", "leaf: B ")],
  "A tree is a game of twenty questions. Each internal node tests one feature against a threshold and sends the example left or right. Leaves hold the predicted class, the majority label of the training points that landed there."),
 eqs("Choosing a split: Gini impurity", [r"$G=1-\sum_k p_k^2$", r"$G_{split}=\frac{n_L}{n}G_L+\frac{n_R}{n}G_R$"], ["Try every feature and threshold", "Keep the split with the lowest weighted impurity"],
  "To pick a question, we measure impurity. Gini is one minus the sum of squared class proportions: zero for a pure node. We try every feature and every threshold, and keep the split whose weighted child impurity is lowest. Then recurse."),
 code("Greedy split search", src(M, "gini") + "\n\n# inside DecisionTree._grow\nfor f in feats:\n    for t in np.unique(X[:, f])[:-1]:\n        left = X[:, f] <= t\n        g = (left.sum() * gini(y[left])\n             + (~left).sum() * gini(y[~left])) / len(y)\n        if best is None or g < best[0]:\n            best = (g, f, t)",
  "In code, the grow function stops at max depth, at small nodes, or when a node is pure, and returns a majority leaf. Otherwise it scans features and thresholds for the lowest weighted Gini, and recurses on both sides."),
 bullets("Random forest", ["Bootstrap: each tree sees a resample of the data", "Each split considers √d random features", "Predict by majority vote across trees", "Averaging de-correlated trees cuts variance"],
  "A single deep tree overfits. A random forest trains many trees, each on a bootstrap sample, and each split only looks at a random subset of about the square root of d features. That de-correlates the trees, and voting across them slashes variance."),
 code("RandomForest.fit", src(M, "RandomForest.fit"), "The forest code draws bootstrap indices, sets max features to the square root of d by default, and trains independent trees with different seeds. Prediction takes the most common vote per example."),
 bullets("Complexity & trade-offs", ["Naive split search: O(d · n²) per node; sort-based O(d · n log n)", "Prediction: O(depth)", "Single tree: interpretable but high variance", "Forest: accurate, robust, less interpretable"],
  "Our straightforward split search re-scans the node for each threshold; sorting with prefix counts brings it to n log n per feature. Prediction is just a walk of depth steps. A single tree is interpretable but unstable; a forest is accurate and robust, at the cost of interpretability."),
 bullets("Recap", ["Trees ask greedy threshold questions", "Split by minimum weighted Gini", "Limit depth to control overfitting", "Forests = bagging + feature subsampling"],
  "To recap: trees greedily choose threshold questions that minimise weighted Gini, depth limits control overfitting, and random forests combine bagging with feature subsampling for strong, stable predictions."),
]
