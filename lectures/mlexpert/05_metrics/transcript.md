# MLExpert · Evaluation Metrics

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Evaluation Metrics (0:00) — `slides/01.png`

A model is only as good as the metric you judge it by. In this lecture we implement the core classification and regression metrics from scratch and talk about when each one is the right choice.

## 2. The problem (0:11) — `slides/02.png`

Imagine a fraud detector that's ninety-nine percent accurate, on data where only one percent is fraud. It could just say no fraud every time. Different mistakes cost different amounts, so we need metrics that reflect the real goal.

## 3. Confusion matrix (0:25) — `slides/03.png`

Everything starts with the confusion matrix. True positives are positives we caught, false negatives are positives we missed, false positives are false alarms, and true negatives are correct rejections.

## 4. Precision, recall, F1 (0:37) — `slides/04.png`

Precision asks: of everything we flagged, how much was real? Recall asks: of all real positives, how many did we find? F1 is their harmonic mean, which is only high when both are. The code guards each division so empty cases return zero.

## 5. Precision / recall / F1 (0:54) — `slides/05.png`

The implementation counts the four cells with boolean masks, then derives precision, recall, and F1, guarding against division by zero.

## 6. ROC AUC: ranking quality (1:03) — `slides/06.png`

ROC AUC measures ranking quality, independent of any threshold. It equals the probability that a randomly chosen positive gets a higher score than a randomly chosen negative, with ties counting half. Point five is a coin flip, one is perfect.

## 7. AUC by pairwise comparison (1:19) — `slides/07.png`

Our version uses that definition directly: compare every positive score with every negative score via broadcasting and average the wins. That's quadratic; a sort-based version is n log n for large data.

## 8. Probabilistic and regression metrics (1:31) — `slides/08.png`

Log loss judges the probabilities themselves and rewards calibration; we clip p away from zero and one to avoid infinite logs. For regression, mean squared error punishes big misses, and R squared compares our errors to simply predicting the mean.

## 9. Recap (1:46) — `slides/09.png`

To recap: accuracy misleads on imbalanced data. Choose between precision and recall based on which error costs more. Use AUC for ranking quality, log loss for calibrated probabilities, and MSE or R squared for regression.
