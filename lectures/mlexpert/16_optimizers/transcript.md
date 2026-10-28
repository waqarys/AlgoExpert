# MLExpert · Gradient Descent Optimizers

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Optimizers (0:00) — `slides/01.png`

Almost every model is trained by some flavour of gradient descent. This lecture walks through four of them, from plain batch descent to Adam, and when to use each.

## 2. The problem (0:10) — `slides/02.png`

We need to minimise a loss over many parameters. Computing the full gradient on big data is expensive, and loss surfaces have narrow ravines where plain gradient descent zig-zags.

## 3. Batch gradient descent (0:21) — `slides/03.png`

Batch gradient descent steps against the full gradient. It's exact but each step touches every example. The learning rate is critical: too large and it diverges, too small and it crawls.

## 4. Batch GD and mini-batch SGD (0:34) — `slides/04.png`

Mini-batch SGD shuffles each epoch and steps on small batches. Gradients are noisy, but you get many updates per pass over the data, and the noise can even help escape poor regions.

## 5. Momentum (0:45) — `slides/05.png`

Momentum keeps a running velocity. Gradients that flip sign across a ravine cancel out, while consistent directions add up. On this elongated bowl, plain descent zig-zags; momentum glides along the valley floor.

## 6. Adam (1:00) — `slides/06.png`

Adam combines momentum with a per-parameter scale. It tracks a running mean of gradients and of squared gradients, corrects both for their zero initialisation, and divides one by the square root of the other, so every parameter gets its own adaptive step size.

## 7. Adam (1:15) — `slides/07.png`

The code follows the equations line by line: update both moments, bias-correct them using the step count t, and take the scaled step.

## 8. Trade-offs (1:23) — `slides/08.png`

Batch descent is stable but slow per step. SGD is cheap and noisy, and often generalises well. Momentum speeds through ravines. Adam is the robust default for deep learning, needing little tuning, though tuned SGD with momentum sometimes generalises better.

## 9. Recap (1:40) — `slides/09.png`

To recap: step against the gradient, use mini-batches to scale, add momentum to smooth the direction, and use Adam to adapt step sizes per parameter.
