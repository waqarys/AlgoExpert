from speclib import *
import numpy as np
TITLE = "MLExpert · Support Vector Machines"; OUT = "mlexpert/12_svm"; M = "mlexpert/mlexpert/svm.py"
def draw(ax):
    r = np.random.default_rng(3); a = r.normal([1.5, 1.5], .5, (20, 2)); b = r.normal([4, 4], .5, (20, 2))
    ax.scatter(*a.T, color="#38bdf8"); ax.scatter(*b.T, color="#f472b6"); x = np.linspace(0, 5.5, 2)
    ax.plot(x, 5.5 - x, color="#e2e8f0", lw=2)
    for o in (-1, 1): ax.plot(x, 5.5 - x + o, color="#94a3b8", ls="--")
SLIDES = [
 title("Support Vector Machines", "Maximum-margin classifiers", "Support vector machines find the separating line that stays as far as possible from both classes. We'll derive the hinge loss and train a linear SVM with the Pegasos algorithm."),
 bullets("The problem", ["Two classes, many separating lines", "Which one generalises best?", "Must tolerate a few overlapping points"],
  "When two classes can be separated, there are infinitely many lines that do it. Which one should we pick? And what if a few points overlap?"),
 plot("Intuition: widest street", draw, ["Pick the boundary with max margin", "Only points on the edge matter:", "the support vectors"],
  "The SVM's answer: choose the widest street. The boundary sits in the middle, and the margin edges touch the closest points, the support vectors. Points far away don't affect the solution at all."),
 eqs("Hinge loss objective", [r"$\min_w\ \frac{\lambda}{2}\|w\|^2+\frac{1}{n}\sum_i\max(0,1-y_i\,w^\top x_i)$"], ["Small ‖w‖ ⇔ wide margin", "Loss is zero once a point is beyond the margin", "Labels are −1 / +1"],
  "In math: keep the weights small, which means a wide margin, while paying a hinge loss for any point inside the margin or on the wrong side. Once a point is safely past the margin, its loss is zero. Lambda balances margin width against violations."),
 bullets("Pegasos: stochastic sub-gradient", ["Step size η_t = 1 / (λ t)", "Always shrink: w ← (1 − ηλ) w", "If margin < 1: w ← w + η y x", "Bias folded in as an extra feature"],
  "Pegasos optimises this with stochastic sub-gradient steps. At step t the learning rate is one over lambda t. Every step shrinks the weights, the regulariser's pull, and if the sampled point violates the margin, we push w toward classifying it correctly."),
 code("LinearSVM.fit", src(M, "LinearSVM.fit"), "The code converts labels to plus and minus one, appends a ones column for the bias, and loops over shuffled samples applying exactly those two updates."),
 bullets("Complexity & trade-offs", ["Pegasos: O(epochs · n · d), independent of margin", "Robust: only support vectors shape the boundary", "Non-linear: kernel trick (RBF, polynomial)", "No native probabilities; scale features"],
  "Each epoch is linear in the data. Because only support vectors matter, SVMs are robust to far-away points. For non-linear boundaries the kernel trick swaps dot products for kernels like RBF. SVMs don't output probabilities natively, and like most margin methods need scaled features."),
 bullets("Recap", ["Maximise the margin", "Hinge loss + L2 penalty", "Pegasos: shrink, then fix violations", "Kernels for non-linear data"],
  "To recap: SVMs maximise the margin by combining hinge loss with an L2 penalty. Pegasos trains them with simple stochastic steps, and kernels extend them to non-linear problems."),
]
