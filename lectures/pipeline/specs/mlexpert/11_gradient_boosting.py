from speclib import *
TITLE = "MLExpert · Gradient Boosting"; OUT = "mlexpert/11_gradient_boosting"; M = "mlexpert/mlexpert/gradient_boosting.py"
SLIDES = [
 title("Gradient Boosting", "Many small trees, each fixing the last", "Gradient boosting is behind XGBoost and LightGBM, the go-to models for tabular data. The idea: add small trees one at a time, each correcting the mistakes of the ensemble so far."),
 bullets("The problem", ["Tabular regression with complex interactions", "One tree: too simple or overfits", "Forests average; can we instead correct errors?"],
  "On tabular data, one tree is either too shallow to capture the pattern or deep enough to overfit. Forests average independent trees. Boosting asks a different question: can each new tree specifically fix what the previous ones got wrong?"),
 eqs("Intuition: fit the residuals", [r"$F_0=\bar y,\qquad F_m=F_{m-1}+\eta\,h_m(x)$", r"$h_m\approx y-F_{m-1}(x)$"], ["For squared loss, residual = negative gradient", "η (learning rate) shrinks each step"],
  "Start with the mean as the prediction. Compute residuals, what's left to explain, and fit a small tree to them. Add that tree, scaled by a learning rate. Repeat. For squared loss, the residual is exactly the negative gradient, so this is gradient descent in function space."),
 code("The boosting loop", src(M, "GradientBoostingRegressor.fit"), "The code is short. Initialise with the mean. Each round, fit a depth-limited regression tree to y minus the current prediction, add its shrunken output, and record the training loss, which should fall steadily."),
 bullets("Regression trees with prefix sums", ["Leaf value = mean of its targets", "Split cost = SSE(left) + SSE(right)", "SSE = Σy² − (Σy)²/n via cumulative sums", "O(n log n) per feature per node"],
  "The base learner is a regression tree whose leaves predict means. To find splits fast, we sort each feature and use cumulative sums of y and y squared, so every candidate split's squared error is computed in constant time."),
 code("Fast split search", "\n".join(l[4:] for l in src(M, "RegressionTree._grow").split("    best = None\n")[1].split("    if best is None:")[0].splitlines()), "Here's that scan. For each feature we sort, build the prefix sums, skip positions where neighbouring values are equal, and compute left plus right squared error in constant time per split."),
 bullets("Complexity & trade-offs", ["Training: O(M · d · n log n) for M trees", "Sequential: harder to parallelise than forests", "Tune: learning rate, #trees, depth (early stopping)", "Usually beats forests on tabular data"],
  "Training costs the number of trees times d times n log n, and it's sequential, unlike forests. You tune the learning rate, number of trees, and depth together, ideally with early stopping on validation loss. When tuned, it usually beats random forests on tabular data."),
 bullets("Recap", ["Start from the mean", "Each tree fits the current residuals", "Shrink with a learning rate", "Gradient descent in function space"],
  "To recap: start from the mean, fit each new tree to the residuals, shrink it with a learning rate, and repeat. It's gradient descent where each step is a tree."),
]
