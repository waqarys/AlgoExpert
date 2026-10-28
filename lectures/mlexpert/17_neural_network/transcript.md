# MLExpert · Neural Networks and Backpropagation

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Neural Networks (0:00) — `slides/01.png`

Neural networks stack simple layers to learn complex functions. In this lecture we build a fully connected network with ReLU and softmax, and derive backpropagation step by step.

## 2. The problem (0:11) — `slides/02.png`

Linear models fail on patterns like XOR, and hand-engineering features doesn't scale. We want a model that learns useful intermediate features by itself.

## 3. Architecture (0:22) — `slides/03.png`

The network is a chain of layers. Each layer multiplies by a weight matrix, adds a bias, and applies a non-linearity: ReLU in hidden layers, softmax at the output, which feeds a cross-entropy loss. Without the non-linearities, the whole stack would collapse into one linear model.

## 4. Forward pass (0:39) — `slides/04.png`

In the forward pass, each layer's activation feeds the next. Weights start with He initialisation, scaled by two over fan-in, which keeps ReLU signals from vanishing or exploding. We cache every activation because backprop needs them.

## 5. Backpropagation (0:54) — `slides/05.png`

Backprop applies the chain rule backwards. With softmax and cross-entropy, the output error is simply probabilities minus one-hot targets. Each weight gradient is the layer's input transposed times its error. The error then flows back through the weights and is masked by where ReLU was active.

## 6. gradients() (1:13) — `slides/06.png`

Here it is in code. Run forward, subtract one at the true class, divide by batch size, then loop backwards: compute weight and bias gradients, and propagate delta through the weights and the ReLU mask.

## 7. Training loop (1:25) — `slides/07.png`

Training is mini-batch SGD: shuffle each epoch, compute gradients on each batch, and step every weight matrix and bias vector.

## 8. Complexity & trade-offs (1:33) — `slides/08.png`

Each pass costs roughly the batch size times the sum of layer weight counts, and backward costs about twice forward. Networks can approximate almost anything, but need lots of data and tuning. Dropout, batch normalisation, Adam, and early stopping are the standard tools.

## 9. Recap (1:50) — `slides/09.png`

To recap: a network stacks linear layers and non-linearities. With softmax and cross-entropy the output error is p minus Y, backprop pushes it backwards with the chain rule, and mini-batch SGD does the learning.
