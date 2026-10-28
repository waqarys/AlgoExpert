# MLExpert · Support Vector Machines

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Support Vector Machines (0:00) — `slides/01.png`

Support vector machines find the separating line that stays as far as possible from both classes. We'll derive the hinge loss and train a linear SVM with the Pegasos algorithm.

## 2. The problem (0:11) — `slides/02.png`

When two classes can be separated, there are infinitely many lines that do it. Which one should we pick? And what if a few points overlap?

## 3. Intuition: widest street (0:21) — `slides/03.png`

The SVM's answer: choose the widest street. The boundary sits in the middle, and the margin edges touch the closest points, the support vectors. Points far away don't affect the solution at all.

## 4. Hinge loss objective (0:33) — `slides/04.png`

In math: keep the weights small, which means a wide margin, while paying a hinge loss for any point inside the margin or on the wrong side. Once a point is safely past the margin, its loss is zero. Lambda balances margin width against violations.

## 5. Pegasos: stochastic sub-gradient (0:49) — `slides/05.png`

Pegasos optimises this with stochastic sub-gradient steps. At step t the learning rate is one over lambda t. Every step shrinks the weights, the regulariser's pull, and if the sampled point violates the margin, we push w toward classifying it correctly.

## 6. LinearSVM.fit (1:05) — `slides/06.png`

The code converts labels to plus and minus one, appends a ones column for the bias, and loops over shuffled samples applying exactly those two updates.

## 7. Complexity & trade-offs (1:14) — `slides/07.png`

Each epoch is linear in the data. Because only support vectors matter, SVMs are robust to far-away points. For non-linear boundaries the kernel trick swaps dot products for kernels like RBF. SVMs don't output probabilities natively, and like most margin methods need scaled features.

## 8. Recap (1:33) — `slides/08.png`

To recap: SVMs maximise the margin by combining hinge loss with an L2 penalty. Pegasos trains them with simple stochastic steps, and kernels extend them to non-linear problems.
