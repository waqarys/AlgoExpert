from speclib import *
import numpy as np
TITLE = "MLExpert · k-Nearest Neighbours"; OUT = "mlexpert/07_knn"; M = "mlexpert/mlexpert/knn.py"
def draw(ax):
    r = np.random.default_rng(1); a = r.normal([2, 2], .8, (25, 2)); b = r.normal([4.5, 4], .8, (25, 2))
    ax.scatter(*a.T, color="#38bdf8"); ax.scatter(*b.T, color="#f472b6"); q = np.array([3.3, 3.0])
    ax.scatter(*q, color="#fbbf24", s=200, marker="*"); X = np.vstack([a, b]); d = ((X - q) ** 2).sum(1)
    for i in np.argsort(d)[:5]: ax.plot([q[0], X[i, 0]], [q[1], X[i, 1]], color="#fbbf24", lw=1)
SLIDES = [
 title("k-Nearest Neighbours", "Predict by asking your neighbours", "k-nearest neighbours may be the simplest model there is: no training at all, just memory and a distance function. Let's see how it works, how to code it, and where it breaks."),
 bullets("The problem", ["Classify or regress a new point", "No assumptions about the shape of the boundary", "Similar inputs should have similar outputs"],
  "We want to label a new point, without assuming a linear boundary or any particular form. The only assumption is that similar inputs have similar outputs."),
 plot("Intuition", draw, ["Find the k closest points", "Classification: majority vote", "Regression: average value"],
  "So, to label the yellow star, find its k closest training points. For classification, take a majority vote of their labels. For regression, average their values. That's the whole algorithm."),
 eqs("Distance", [r"$d(x,x')=\sqrt{\sum_j (x_j-x'_j)^2}$"], ["Scale features first, or one feature dominates", "Odd k avoids ties in binary problems", "Small k: noisy; large k: over-smoothed"],
  "We use Euclidean distance, so feature scaling is essential, otherwise the feature with the biggest units dominates. Choose k by cross-validation: small k follows noise, large k blurs the boundary. An odd k avoids ties in two-class problems."),
 code("Implementation", src(M, "KNN.predict"), "Fit just stores the data. Predict computes all pairwise squared distances with broadcasting, takes the k smallest with argsort, and either averages the neighbours' values or picks the most common label."),
 bullets("Complexity & trade-offs", ["Training O(1); prediction O(n·d) per query", "Memory: stores the whole dataset", "Curse of dimensionality: distances lose meaning", "Speed-ups: KD-trees, ball trees, approximate NN"],
  "Training is free, but each prediction scans all n points, so it's order n times d per query, and the whole dataset sits in memory. In high dimensions all distances look similar, which hurts accuracy. KD-trees or approximate nearest-neighbour indexes speed things up."),
 bullets("Recap", ["Lazy learner: store, then vote or average", "Scale features; tune k", "Cheap to train, expensive to query", "Great baseline for low-dimensional data"],
  "To recap: k-NN stores the data and votes or averages at query time. Scale features and tune k. It's cheap to train but expensive to query, and a solid baseline in low dimensions."),
]
