# MLExpert · Cross-Validation and Bias-Variance

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Model Selection (0:00) — `slides/01.png`

How do you choose between models, or pick a hyper-parameter, without fooling yourself? This lecture covers k-fold cross-validation and the bias-variance decomposition, with code for both.

## 2. The problem (0:11) — `slides/02.png`

A single split gives a noisy estimate, and tuning against the test set quietly leaks it into training. Underneath sits a deeper tension: complex models chase noise, simple ones miss real structure.

## 3. k-fold cross-validation (0:24) — `slides/03.png`

K-fold cross-validation splits the data into k folds. Each fold takes a turn as validation while a fresh model trains on the rest. Averaging the k scores gives a far more stable estimate, and the spread tells you how much to trust it.

## 4. cross_val_score (0:39) — `slides/04.png`

The code takes a factory that builds a new model, so no state leaks between folds. It validates k, defaults to accuracy, and returns all k scores.

## 5. Bias-variance decomposition (0:49) — `slides/05.png`

Expected squared error splits into three parts. Bias squared: how far the average model is from the truth. Variance: how much the model jumps around when trained on different samples. And noise, which no model can remove.

## 6. Measuring it empirically (1:04) — `slides/06.png`

We can measure this. Draw two hundred noisy training sets, fit a polynomial model to each, and predict on a fixed grid. The mean prediction's error gives bias, the spread across fits gives variance.

## 7. What you see (1:18) — `slides/07.png`

Run it across degrees and the classic picture appears. Low-degree polynomials underfit with high bias. High degrees overfit with high variance. The best model minimises the sum, and more data or regularisation pushes variance down.

## 8. Recap (1:34) — `slides/08.png`

To recap: use k-fold cross-validation to compare and tune models, keep a final test set untouched, and think of error as bias squared plus variance plus noise. The price is training k times.
