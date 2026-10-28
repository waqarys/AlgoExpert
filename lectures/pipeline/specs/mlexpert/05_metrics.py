from speclib import *
TITLE = "MLExpert · Evaluation Metrics"; OUT = "mlexpert/05_metrics"; M = "mlexpert/mlexpert/metrics.py"
SLIDES = [
 title("Evaluation Metrics", "Measuring what actually matters", "A model is only as good as the metric you judge it by. In this lecture we implement the core classification and regression metrics from scratch and talk about when each one is the right choice."),
 bullets("The problem", ["99% accuracy can be useless (1% fraud rate)", "Errors have different costs", "Need metrics that match the business goal"],
  "Imagine a fraud detector that's ninety-nine percent accurate, on data where only one percent is fraud. It could just say no fraud every time. Different mistakes cost different amounts, so we need metrics that reflect the real goal."),
 bullets("Confusion matrix", ["TP: caught positives      FN: missed positives", "FP: false alarms           TN: correct negatives", "Layout here: [[TN, FP], [FN, TP]]"],
  "Everything starts with the confusion matrix. True positives are positives we caught, false negatives are positives we missed, false positives are false alarms, and true negatives are correct rejections."),
 eqs("Precision, recall, F1", [r"$P=\frac{TP}{TP+FP}\quad R=\frac{TP}{TP+FN}$", r"$F_1=\frac{2PR}{P+R}$"], ["Precision: how many alarms were real", "Recall: how many positives we found"],
  "Precision asks: of everything we flagged, how much was real? Recall asks: of all real positives, how many did we find? F1 is their harmonic mean, which is only high when both are. The code guards each division so empty cases return zero."),
 code("Precision / recall / F1", src(M, "confusion_matrix", "precision_recall_f1"), "The implementation counts the four cells with boolean masks, then derives precision, recall, and F1, guarding against division by zero."),
 bullets("ROC AUC: ranking quality", ["AUC = P(random positive scores > random negative)", "Ties count half; threshold-free", "0.5 = random, 1.0 = perfect ranking"],
  "ROC AUC measures ranking quality, independent of any threshold. It equals the probability that a randomly chosen positive gets a higher score than a randomly chosen negative, with ties counting half. Point five is a coin flip, one is perfect."),
 code("AUC by pairwise comparison", src(M, "roc_auc"), "Our version uses that definition directly: compare every positive score with every negative score via broadcasting and average the wins. That's quadratic; a sort-based version is n log n for large data."),
 eqs("Probabilistic and regression metrics", [r"$\mathrm{LogLoss}=-\overline{y\log p+(1-y)\log(1-p)}$", r"$R^2=1-\frac{SS_{res}}{SS_{tot}}$"], ["Log loss rewards calibrated probabilities (clip p)", "MSE punishes large errors; R² vs predicting the mean"],
  "Log loss judges the probabilities themselves and rewards calibration; we clip p away from zero and one to avoid infinite logs. For regression, mean squared error punishes big misses, and R squared compares our errors to simply predicting the mean."),
 bullets("Recap", ["Accuracy misleads on imbalanced data", "Precision vs recall: pick by cost of errors", "AUC for ranking, log loss for calibration", "MSE / R² for regression"],
  "To recap: accuracy misleads on imbalanced data. Choose between precision and recall based on which error costs more. Use AUC for ranking quality, log loss for calibrated probabilities, and MSE or R squared for regression."),
]
