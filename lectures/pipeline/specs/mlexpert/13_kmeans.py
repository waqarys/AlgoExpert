from speclib import *
import numpy as np
TITLE = "MLExpert · k-Means Clustering"; OUT = "mlexpert/13_kmeans"; M = "mlexpert/mlexpert/kmeans.py"
def draw(ax):
    r = np.random.default_rng(2); C = np.array([[1, 1], [4, 1.5], [2.5, 4]]); cols = ["#38bdf8", "#f472b6", "#34d399"]
    for c, col in zip(C, cols):
        p = r.normal(c, .5, (30, 2)); ax.scatter(*p.T, color=col, s=20); ax.scatter(*p.mean(0), color="#fbbf24", marker="X", s=200)
SLIDES = [
 title("k-Means", "Clustering with k-means++", "k-means is the go-to clustering algorithm: group unlabeled points into k clusters around centres. We'll cover Lloyd's algorithm and the smarter k-means plus plus initialisation."),
 bullets("The problem", ["Unlabeled data", "Group similar points together", "k is chosen in advance"],
  "Here there are no labels. We just want to discover groups, say customer segments, where points in a group are close to each other. We decide the number of groups, k, up front."),
 plot("Intuition", draw, ["Each cluster has a centre", "Points join the nearest centre", "Centres move to their members' mean"],
  "Each cluster is represented by a centre. Every point belongs to its nearest centre, and each centre sits at the mean of its points. Those two conditions define a good clustering."),
 eqs("Objective and Lloyd's algorithm", [r"$\min\ \sum_i \|x_i-\mu_{c(i)}\|^2$"], ["Assign: each point → nearest centre", "Update: centre ← mean of its points", "Repeat until centres stop moving"],
  "We minimise the total squared distance to assigned centres, called inertia. Lloyd's algorithm alternates two steps: assign each point to its nearest centre, then move each centre to its points' mean. Each step can only lower inertia, so it converges, though to a local minimum."),
 bullets("k-means++ initialisation", ["First centre: random point", "Next: sample with probability ∝ D(x)²", "Spreads centres out → better, faster results"],
  "Initialisation matters. k-means plus plus picks the first centre at random, then samples each next centre with probability proportional to the squared distance from the nearest centre chosen so far. Far-away points are likely picks, which spreads the centres out."),
 code("Implementation", src(M, "KMeans._init", "KMeans.fit"), "Here's the code. The init function implements k-means plus plus. Fit alternates predict, which assigns nearest centres, with the mean update, keeping an empty cluster's centre in place, and stops when the largest shift is below a tolerance."),
 bullets("Complexity & trade-offs", ["O(n · k · d) per iteration", "Local minima: run several seeds", "Assumes round, similar-size clusters", "Pick k with the elbow method or silhouette"],
  "Each iteration costs n times k times d. Results depend on initialisation, so run a few seeds and keep the lowest inertia. k-means assumes roughly spherical clusters of similar size, and you choose k with the elbow method or silhouette score."),
 bullets("Recap", ["Alternate assign and update", "Minimises within-cluster squared distance", "k-means++ for a good start", "Fast and simple"],
  "To recap: k-means alternates assigning points and updating centres to minimise within-cluster squared distance. Start with k-means plus plus, and you have a fast, simple clustering method."),
]
