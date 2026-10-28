import numpy as np
TITLE = "MLExpert · Linear Regression"
OUT = "mlexpert/linear_regression"
rng = np.random.default_rng(0)
X = rng.uniform(0, 10, 40); Y = 2.5 * X + 4 + rng.normal(0, 3, 40)

def scatter(ax):
    ax.scatter(X, Y, color="#38bdf8", s=30); ax.set_xlabel("square metres (x100)"); ax.set_ylabel("price")
def fit(ax):
    scatter(ax); w, b = np.polyfit(X, Y, 1); xs = np.array([0, 10])
    ax.plot(xs, w * xs + b, color="#f472b6", lw=3)
    for x, y in zip(X[:12], Y[:12]): ax.plot([x, x], [y, w * x + b], color="#fbbf24", lw=1, alpha=.8)
def gd(ax):
    w = b = 0.0; L = []
    for _ in range(60):
        e = w * X + b - Y; L.append((e ** 2).mean())
        w -= 0.01 * 2 * (X * e).mean(); b -= 0.01 * 2 * e.mean()
    ax.plot(L, color="#34d399", lw=3); ax.set_yscale("log"); ax.set_xlabel("epoch"); ax.set_ylabel("MSE")

SLIDES = [
 dict(kind="title", heading="Linear Regression", subtitle="Fitting the best straight line, two ways",
      narration="Welcome. In this lecture we build linear regression from scratch, the simplest and most useful model in machine learning. We'll solve it two ways: with a closed-form equation, and with gradient descent."),
 dict(kind="plot", heading="The problem", draw=scatter,
      bullets=["Input: features X", "Output: a number y", "Goal: predict y for", "  new, unseen X"],
      narration="Here's the problem. We have examples, say house sizes and their prices, and we want to predict the price of a house we haven't seen. The inputs are features, the output is a continuous number."),
 dict(kind="equations", heading="Intuition: a weighted sum",
      equations=[r"$\hat{y} = w_1x_1 + \dots + w_dx_d + b = Xw + b$"],
      bullets=["Each weight says how much a feature pushes the prediction", "The bias b is the baseline when every feature is zero"],
      narration="The intuition: a prediction is just a weighted sum of the features plus a bias. Each weight says how strongly its feature pushes the prediction up or down. Learning means choosing those weights well."),
 dict(kind="plot", heading="What does 'best' mean?", draw=fit,
      bullets=["Residual = prediction − truth", "Minimise mean squared error:", r"$\mathrm{MSE}=\frac{1}{n}\sum_i(\hat{y}_i-y_i)^2$"],
      narration="So what is the best line? We measure the vertical gaps, the residuals, between each point and the line. We square them, so big misses cost a lot, and average them. That's the mean squared error, and we want it as small as possible."),
 dict(kind="equations", heading="Way 1: the normal equation",
      equations=[r"$L(\theta)=\frac{1}{n}\|X_b\theta-y\|^2$", r"$\theta=(X_b^\top X_b+\lambda I')^{-1}X_b^\top y$"],
      bullets=["Append a column of ones so the bias lives inside θ", "Set the gradient to zero → solve one linear system"],
      narration="Way one is exact. Append a column of ones to X so the bias becomes just another weight. The loss is a smooth bowl, so we set its gradient to zero and get the normal equation. The optional lambda term adds ridge regularisation, and we don't penalise the bias."),
 dict(kind="code", heading="Closed form in NumPy", code='''
Xb = np.hstack([X, np.ones((n, 1))])        # add bias column
reg = self.l2 * np.eye(d + 1)
reg[-1, -1] = 0                             # don't regularise bias
theta = np.linalg.solve(Xb.T @ Xb + reg, Xb.T @ y)
self.w, self.b = theta[:-1], theta[-1]
''', narration="In code it's four lines. Build X with the bias column, build the regulariser with a zero in the bias corner, and call solve rather than computing an explicit inverse, which is faster and numerically safer. Then split theta back into weights and bias."),
 dict(kind="plot", heading="Way 2: gradient descent", draw=gd,
      bullets=[r"$\nabla_w = \frac{2}{n}X^\top(Xw+b-y)$", r"$w \leftarrow w-\eta\,\nabla_w$", "Repeat for many epochs"],
      narration="Way two is iterative. Start with zero weights, compute the error, and step each weight against its gradient, scaled by the learning rate. The loss drops quickly, as the curve shows. This scales to huge datasets where solving a big matrix system is too expensive."),
 dict(kind="code", heading="Gradient descent loop", code='''
self.w, self.b = np.zeros(d), 0.0
for _ in range(self.epochs):
    err = X @ self.w + self.b - y
    self.w -= self.lr * (2 * X.T @ err / n + 2 * self.l2 * self.w)
    self.b -= self.lr * 2 * err.mean()
''', narration="The loop is short too. Each epoch computes the residuals once, then updates the weights with the mean squared error gradient plus the ridge term, and updates the bias with the mean residual."),
 dict(kind="bullets", heading="Worked example",
      bullets=["Points: (1, 3), (2, 5), (3, 7)", "Means: x̄ = 2, ȳ = 5",
               "w = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)² = 4 / 2 = 2", "b = ȳ − w·x̄ = 5 − 4 = 1  →  ŷ = 2x + 1", "Residuals all zero: MSE = 0"],
      narration="A tiny worked example. Take the points one three, two five, and three seven. The means are two and five. With one feature, the normal equation reduces to covariance over variance: four divided by two, so the slope is two. The intercept is five minus two times two, which is one. So y hat equals two x plus one, and every residual is zero."),
 dict(kind="bullets", heading="Complexity & trade-offs",
      bullets=["Normal equation: O(n·d² + d³) — exact, no tuning, slow for large d",
               "Gradient descent: O(n·d) per epoch — scales, needs learning rate & scaling",
               "Ridge (λ>0) fixes ill-conditioned XᵀX and reduces overfitting",
               "Assumes a linear relationship; sensitive to outliers"], size=22,
      narration="Trade-offs. The normal equation costs n d squared plus d cubed: exact and tuning-free, but slow with many features. Gradient descent costs n times d per epoch and scales well, but needs a good learning rate and scaled features. Ridge keeps the system well-conditioned. And remember, the model assumes a linear relationship and squared error makes it sensitive to outliers."),
 dict(kind="bullets", heading="Recap",
      bullets=["Prediction = weighted sum + bias", "Train by minimising mean squared error",
               "Closed form: solve (XᵀX + λI)θ = Xᵀy", "Gradient descent: step against the gradient"],
      narration="To recap: linear regression predicts with a weighted sum plus bias, trains by minimising mean squared error, and can be solved exactly with the normal equation or iteratively with gradient descent. Next up, logistic regression, which bends this idea into classification."),
]
