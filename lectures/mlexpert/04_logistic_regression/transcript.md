# MLExpert · Logistic Regression

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Logistic Regression (0:00) — `slides/01.png`

Logistic regression takes the weighted sum from linear regression and turns it into a probability. It's the workhorse baseline for classification, and we'll build both the binary and the multi-class version.

## 2. The problem (0:12) — `slides/02.png`

The task: predict a class, such as spam or not spam, and ideally a probability we can trust. A plain linear model can output values below zero or above one, which make no sense as probabilities. We need to squash the output.

## 3. Intuition: squash with a sigmoid (0:27) — `slides/03.png`

The sigmoid does exactly that. Any real score goes in, a number between zero and one comes out. A score of zero means fifty-fifty, so the decision boundary is the line where the weighted sum equals zero. Clipping the input keeps the exponent numerically safe.

## 4. Loss: cross-entropy (0:44) — `slides/04.png`

We train by minimising cross-entropy, which heavily punishes confident wrong answers. The beautiful part is the gradient: X transpose times prediction minus truth, the same shape as linear regression. The loss is convex, so gradient descent reaches the global optimum.

## 5. Binary training loop (1:01) — `slides/05.png`

Here's the loop. Compute probabilities, then step the weights by X transpose times the error, plus an optional L2 term, and step the bias by the mean error. Prediction thresholds the probability, by default at one half.

## 6. Multi-class: softmax (1:16) — `slides/06.png`

For more than two classes we use softmax. Each class gets its own weight vector and score, and softmax turns the scores into a distribution. Subtracting the max score first prevents overflow. With one-hot targets, the gradient is again X transpose times P minus Y.

## 7. Softmax regression (1:34) — `slides/07.png`

The code mirrors the binary case: build one-hot targets, compute softmax probabilities, and update the weight matrix and biases with the averaged error.

## 8. Complexity & trade-offs (1:43) — `slides/08.png`

Each epoch costs n times d times the number of classes, and prediction is a single dot product. Weights are interpretable as log-odds. The limitation is a linear boundary, unless you add feature crosses. And remember the threshold is a knob: move it to trade precision for recall.

## 9. Recap (2:02) — `slides/09.png`

To recap: sigmoid or softmax turn linear scores into probabilities, we minimise cross-entropy, and the gradient is X transpose times the error. It's the fast, interpretable baseline to try first.
