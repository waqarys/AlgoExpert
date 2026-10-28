# MLExpert · Ridge, Lasso and Elastic Net

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Regularisation (0:00) — `slides/01.png`

Linear regression can overfit, especially with many correlated features. Regularisation fixes that by penalising large weights. We'll build ridge, lasso, and elastic net from scratch.

## 2. The problem (0:13) — `slides/02.png`

Here's the issue. With many features and limited data, least squares can produce huge weights that fit noise. Correlated features make the matrix X transpose X nearly singular, so tiny data changes swing the solution. We want to trade a little bias for a lot less variance.

## 3. Three penalties (0:31) — `slides/03.png`

Ridge adds the squared length of the weights. Lasso adds the sum of absolute values. Elastic net blends the two with a mixing ratio. The intuition: ridge shrinks every weight smoothly, while lasso pushes some weights exactly to zero, giving feature selection for free.

## 4. Ridge: closed form (0:48) — `slides/04.png`

Ridge keeps a closed form. We centre X and y so the intercept isn't penalised, then solve X transpose X plus alpha times identity against X transpose y. Adding alpha makes the system always solvable. The bias is recovered from the means.

## 5. Lasso: soft thresholding (1:03) — `slides/05.png`

Lasso has no closed form because absolute value has a kink at zero. Instead we use coordinate descent: fix all weights but one, and solve for that one exactly. The answer is the soft-threshold function, which shrinks the value toward zero and clips anything smaller than gamma to exactly zero.

## 6. Coordinate descent (1:22) — `slides/06.png`

In code, for each feature we compute the partial residual, leaving that feature out, correlate it with the feature, soft-threshold by the L1 strength, and divide by the column's energy plus the L2 strength. Loop until the weights stop changing.

## 7. Trade-offs (1:36) — `slides/07.png`

Trade-offs. Ridge is one linear solve and handles collinearity, but keeps every feature. Lasso gives sparse, interpretable models, though among correlated features it picks one somewhat arbitrarily. Elastic net combines sparsity with stability. In every case, scale features first and choose alpha by cross-validation.

## 8. Recap (1:57) — `slides/08.png`

To recap: regularisation penalises weights to reduce variance. L2 shrinks, L1 zeroes out. Ridge is solved in closed form, lasso by coordinate descent with soft thresholding, and elastic net blends the two.
