# MLExpert · Linear Regression

Voice: en-US-GuyNeural. Video: [lecture.mp4](lecture.mp4)

## 1. Linear Regression (0:00)

Welcome. In this lecture we build linear regression from scratch, the simplest and most useful model in machine learning. We'll solve it two ways: with a closed-form equation, and with gradient descent.

## 2. The problem (0:13)

Here's the problem. We have examples, say house sizes and their prices, and we want to predict the price of a house we haven't seen. The inputs are features, the output is a continuous number.

## 3. Intuition: a weighted sum (0:25)

The intuition: a prediction is just a weighted sum of the features plus a bias. Each weight says how strongly its feature pushes the prediction up or down. Learning means choosing those weights well.

## 4. What does 'best' mean? (0:38)

So what is the best line? We measure the vertical gaps, the residuals, between each point and the line. We square them, so big misses cost a lot, and average them. That's the mean squared error, and we want it as small as possible.

## 5. Way 1: the normal equation (0:53)

Way one is exact. Append a column of ones to X so the bias becomes just another weight. The loss is a smooth bowl, so we set its gradient to zero and get the normal equation. The optional lambda term adds ridge regularisation, and we don't penalise the bias.

## 6. Closed form in NumPy (1:11)

In code it's four lines. Build X with the bias column, build the regulariser with a zero in the bias corner, and call solve rather than computing an explicit inverse, which is faster and numerically safer. Then split theta back into weights and bias.

## 7. Way 2: gradient descent (1:26)

Way two is iterative. Start with zero weights, compute the error, and step each weight against its gradient, scaled by the learning rate. The loss drops quickly, as the curve shows. This scales to huge datasets where solving a big matrix system is too expensive.

## 8. Gradient descent loop (1:44)

The loop is short too. Each epoch computes the residuals once, then updates the weights with the mean squared error gradient plus the ridge term, and updates the bias with the mean residual.

## 9. Worked example (1:55)

A tiny worked example. Take the points one three, two five, and three seven. The means are two and five. With one feature, the normal equation reduces to covariance over variance: four divided by two, so the slope is two. The intercept is five minus two times two, which is one. So y hat equals two x plus one, and every residual is zero.

## 10. Complexity & trade-offs (2:19)

Trade-offs. The normal equation costs n d squared plus d cubed: exact and tuning-free, but slow with many features. Gradient descent costs n times d per epoch and scales well, but needs a good learning rate and scaled features. Ridge keeps the system well-conditioned. And remember, the model assumes a linear relationship and squared error makes it sensitive to outliers.

## 11. Recap (2:43)

To recap: linear regression predicts with a weighted sum plus bias, trains by minimising mean squared error, and can be solved exactly with the normal equation or iteratively with gradient descent. Next up, logistic regression, which bends this idea into classification.
