from speclib import *
import numpy as np
TITLE = "MLExpert · Principal Component Analysis"; OUT = "mlexpert/14_pca"; M = "mlexpert/mlexpert/pca.py"
def draw(ax):
    r = np.random.default_rng(0); X = r.multivariate_normal([0, 0], [[3, 2.2], [2.2, 2]], 150)
    ax.scatter(*X.T, s=12, color="#38bdf8", alpha=.7); _, s, vt = np.linalg.svd(X - X.mean(0), full_matrices=False)
    for v, sv, col in zip(vt, s, ["#f472b6", "#fbbf24"]): ax.arrow(0, 0, *(v * sv / 6), width=.05, color=col)
    ax.set_aspect("equal")
SLIDES = [
 title("PCA", "Principal Component Analysis via SVD", "Principal component analysis compresses data into fewer dimensions while keeping as much variation as possible. We'll see the geometry and a clean implementation using SVD."),
 bullets("The problem", ["Hundreds of correlated features", "Hard to visualise, slow to train", "Want fewer features, minimal information loss"],
  "Datasets often have hundreds of correlated features. They're hard to visualise and slow to model. We'd like a few new features that keep most of the information."),
 plot("Intuition: directions of spread", draw, ["PC1: direction of most variance", "PC2: next, orthogonal to PC1", "Project onto the top k"],
  "Look at this cloud. The pink arrow points along the direction of greatest spread: the first principal component. The second is perpendicular and captures what's left. Projecting onto the top few components keeps the shape while dropping dimensions."),
 eqs("Via SVD", [r"$X-\mu=U\Sigma V^\top$", r"$Z=(X-\mu)\,V_k,\quad \mathrm{var}_i=\frac{\sigma_i^2}{n-1}$"], ["Rows of Vᵀ are the components", "Explained variance ratio = σᵢ² / Σσ²"],
  "Centre the data and take its singular value decomposition. The rows of V transpose are the principal directions, sorted by singular value. Each component's variance is its singular value squared over n minus one, which gives the explained variance ratio."),
 code("PCA", src(M, "PCA"), "The implementation centres, calls SVD with thin matrices, keeps the top components, and computes the explained variance ratio. Transform projects onto the components, and inverse transform maps back, giving a reconstruction."),
 bullets("Complexity & trade-offs", ["Thin SVD: O(n · d · min(n, d))", "Scale features first if units differ", "Linear only; components can be hard to interpret", "Choose k to keep e.g. 95% variance"],
  "A thin SVD costs n times d times the smaller of n and d. Scale features first, otherwise large-unit features dominate. PCA is linear, and components mix features so they can be hard to interpret. A common rule is to keep enough components for ninety-five percent of the variance."),
 bullets("Recap", ["Centre, SVD, keep top-k directions", "Components are orthogonal, ordered by variance", "Use for compression, visualisation, denoising"],
  "To recap: centre the data, run SVD, and keep the top k directions. They're orthogonal and ordered by variance, useful for compression, visualisation, and denoising."),
]
