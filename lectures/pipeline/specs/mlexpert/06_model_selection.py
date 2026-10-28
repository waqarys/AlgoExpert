from speclib import *
TITLE = "MLExpert · Cross-Validation and Bias-Variance"; OUT = "mlexpert/06_model_selection"; M = "mlexpert/mlexpert/model_selection.py"
SLIDES = [
 title("Model Selection", "Cross-validation and the bias-variance trade-off", "How do you choose between models, or pick a hyper-parameter, without fooling yourself? This lecture covers k-fold cross-validation and the bias-variance decomposition, with code for both."),
 bullets("The problem", ["One train/test split is noisy", "Tuning on the test set leaks information", "Complex models fit noise; simple ones miss signal"],
  "A single split gives a noisy estimate, and tuning against the test set quietly leaks it into training. Underneath sits a deeper tension: complex models chase noise, simple ones miss real structure."),
 bullets("k-fold cross-validation", ["Split data into k folds", "Train on k−1 folds, validate on the held-out one", "Repeat k times; report mean ± std", "Fresh, unfitted model every fold"],
  "K-fold cross-validation splits the data into k folds. Each fold takes a turn as validation while a fresh model trains on the rest. Averaging the k scores gives a far more stable estimate, and the spread tells you how much to trust it."),
 code("cross_val_score", src(M, "cross_val_score"), "The code takes a factory that builds a new model, so no state leaks between folds. It validates k, defaults to accuracy, and returns all k scores."),
 eqs("Bias-variance decomposition", [r"$E[(y-\hat f)^2]=\mathrm{Bias}^2+\mathrm{Var}+\sigma^2$"], ["Bias: error of the average model", "Variance: how much the model moves between datasets", "σ²: irreducible noise"],
  "Expected squared error splits into three parts. Bias squared: how far the average model is from the truth. Variance: how much the model jumps around when trained on different samples. And noise, which no model can remove."),
 code("Measuring it empirically", src(M, "bias_variance"), "We can measure this. Draw two hundred noisy training sets, fit a polynomial model to each, and predict on a fixed grid. The mean prediction's error gives bias, the spread across fits gives variance."),
 bullets("What you see", ["Low degree: high bias, low variance (underfit)", "High degree: low bias, high variance (overfit)", "Sweet spot minimises their sum", "More data or regularisation lowers variance"],
  "Run it across degrees and the classic picture appears. Low-degree polynomials underfit with high bias. High degrees overfit with high variance. The best model minimises the sum, and more data or regularisation pushes variance down."),
 bullets("Recap", ["Use k-fold CV to compare and tune models", "Keep a final test set untouched", "Error = bias² + variance + noise", "Cost: k × training time"],
  "To recap: use k-fold cross-validation to compare and tune models, keep a final test set untouched, and think of error as bias squared plus variance plus noise. The price is training k times."),
]
