from speclib import *
import numpy as np
TITLE = "MLExpert · Logistic Regression"; OUT = "mlexpert/04_logistic_regression"; M = "mlexpert/mlexpert/logistic_regression.py"
def sig(ax):
    z = np.linspace(-8, 8, 200); ax.plot(z, 1 / (1 + np.exp(-z)), color="#38bdf8", lw=3)
    ax.axhline(0.5, color="#f472b6", ls="--"); ax.set_xlabel("z = w·x + b"); ax.set_ylabel("P(y=1)")
SLIDES = [
 title("Logistic Regression", "Linear models for classification", "Logistic regression takes the weighted sum from linear regression and turns it into a probability. It's the workhorse baseline for classification, and we'll build both the binary and the multi-class version."),
 bullets("The problem", ["Predict a class, e.g. spam vs not spam", "Want a calibrated probability, not just a label", "Linear regression outputs can be < 0 or > 1"],
  "The task: predict a class, such as spam or not spam, and ideally a probability we can trust. A plain linear model can output values below zero or above one, which make no sense as probabilities. We need to squash the output."),
 plot("Intuition: squash with a sigmoid", sig, [r"$\sigma(z)=\frac{1}{1+e^{-z}}$", "Maps any score to (0, 1)", "Boundary where z = 0"],
  "The sigmoid does exactly that. Any real score goes in, a number between zero and one comes out. A score of zero means fifty-fifty, so the decision boundary is the line where the weighted sum equals zero. Clipping the input keeps the exponent numerically safe."),
 eqs("Loss: cross-entropy", [r"$L=-\frac{1}{n}\sum_i\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right]$", r"$\nabla_w L=\frac{1}{n}X^\top(p-y)$"], ["Convex → gradient descent finds the global optimum"],
  "We train by minimising cross-entropy, which heavily punishes confident wrong answers. The beautiful part is the gradient: X transpose times prediction minus truth, the same shape as linear regression. The loss is convex, so gradient descent reaches the global optimum."),
 code("Binary training loop", src(M, "LogisticRegression.fit"), "Here's the loop. Compute probabilities, then step the weights by X transpose times the error, plus an optional L2 term, and step the bias by the mean error. Prediction thresholds the probability, by default at one half."),
 eqs("Multi-class: softmax", [r"$P(y=k)=\frac{e^{z_k}}{\sum_j e^{z_j}}$"], ["One weight vector per class", "Subtract max(z) for numerical stability", "Same gradient form: Xᵀ(P − Y)"],
  "For more than two classes we use softmax. Each class gets its own weight vector and score, and softmax turns the scores into a distribution. Subtracting the max score first prevents overflow. With one-hot targets, the gradient is again X transpose times P minus Y."),
 code("Softmax regression", src(M, "softmax", "SoftmaxRegression.fit"), "The code mirrors the binary case: build one-hot targets, compute softmax probabilities, and update the weight matrix and biases with the averaged error."),
 bullets("Complexity & trade-offs", ["Training: O(n·d·k) per epoch; prediction O(d·k)", "Interpretable weights (log-odds)", "Only linear boundaries unless you engineer features", "Tune the threshold for precision vs recall"],
  "Each epoch costs n times d times the number of classes, and prediction is a single dot product. Weights are interpretable as log-odds. The limitation is a linear boundary, unless you add feature crosses. And remember the threshold is a knob: move it to trade precision for recall."),
 bullets("Recap", ["Sigmoid / softmax turn scores into probabilities", "Minimise cross-entropy", "Gradient = Xᵀ(p − y)", "Strong, fast, interpretable baseline"],
  "To recap: sigmoid or softmax turn linear scores into probabilities, we minimise cross-entropy, and the gradient is X transpose times the error. It's the fast, interpretable baseline to try first."),
]
