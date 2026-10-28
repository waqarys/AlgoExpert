from speclib import *
import numpy as np
TITLE = "MLExpert · Gradient Descent Optimizers"; OUT = "mlexpert/16_optimizers"; M = "mlexpert/mlexpert/optimizers.py"
def draw(ax):
    a, b = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100)); ax.contour(a, b, a ** 2 + 8 * b ** 2, 12, colors="#334155")
    for name, col, beta in [("GD", "#38bdf8", 0), ("Momentum", "#f472b6", .8)]:
        w = np.array([-2.8, 2.0]); v = np.zeros(2); P = [w.copy()]
        for _ in range(25):
            g = np.array([2 * w[0], 16 * w[1]]); v = beta * v + g; w = w - .055 * v; P.append(w.copy())
        P = np.array(P); ax.plot(*P.T, "-o", ms=3, color=col, label=name)
    ax.legend(facecolor="#1e293b", labelcolor="#e2e8f0")
SLIDES = [
 title("Optimizers", "Batch GD, SGD, Momentum and Adam", "Almost every model is trained by some flavour of gradient descent. This lecture walks through four of them, from plain batch descent to Adam, and when to use each."),
 bullets("The problem", ["Minimise a loss L(w) over many parameters", "Full gradients are expensive on big data", "Ravines and noise slow plain descent"],
  "We need to minimise a loss over many parameters. Computing the full gradient on big data is expensive, and loss surfaces have narrow ravines where plain gradient descent zig-zags."),
 eqs("Batch gradient descent", [r"$w\leftarrow w-\eta\,\nabla L(w)$"], ["Exact gradient over all n examples", "Learning rate η: too big diverges, too small crawls"],
  "Batch gradient descent steps against the full gradient. It's exact but each step touches every example. The learning rate is critical: too large and it diverges, too small and it crawls."),
 code("Batch GD and mini-batch SGD", src(M, "batch_gd", "minibatch_sgd"), "Mini-batch SGD shuffles each epoch and steps on small batches. Gradients are noisy, but you get many updates per pass over the data, and the noise can even help escape poor regions."),
 plot("Momentum", draw, [r"$v\leftarrow\beta v+\nabla L$", r"$w\leftarrow w-\eta v$", "Damps zig-zags", "Accelerates along valleys"],
  "Momentum keeps a running velocity. Gradients that flip sign across a ravine cancel out, while consistent directions add up. On this elongated bowl, plain descent zig-zags; momentum glides along the valley floor."),
 eqs("Adam", [r"$m\leftarrow\beta_1 m+(1-\beta_1)g,\quad v\leftarrow\beta_2 v+(1-\beta_2)g^2$", r"$w\leftarrow w-\eta\,\frac{\hat m}{\sqrt{\hat v}+\epsilon}$"], ["Per-parameter step sizes", "Bias correction: m̂ = m / (1 − β₁ᵗ)"],
  "Adam combines momentum with a per-parameter scale. It tracks a running mean of gradients and of squared gradients, corrects both for their zero initialisation, and divides one by the square root of the other, so every parameter gets its own adaptive step size."),
 code("Adam", src(M, "adam"), "The code follows the equations line by line: update both moments, bias-correct them using the step count t, and take the scaled step."),
 bullets("Trade-offs", ["Batch GD: stable, slow per step", "SGD: cheap steps, noisy; great generalisation", "Momentum: faster through ravines", "Adam: robust default, little tuning"],
  "Batch descent is stable but slow per step. SGD is cheap and noisy, and often generalises well. Momentum speeds through ravines. Adam is the robust default for deep learning, needing little tuning, though tuned SGD with momentum sometimes generalises better."),
 bullets("Recap", ["Step against the gradient", "Mini-batches for scale", "Momentum smooths direction", "Adam adapts step size per parameter"],
  "To recap: step against the gradient, use mini-batches to scale, add momentum to smooth the direction, and use Adam to adapt step sizes per parameter."),
]
