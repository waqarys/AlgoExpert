from speclib import *
TITLE = "MLExpert · Neural Networks and Backpropagation"; OUT = "mlexpert/17_neural_network"; M = "mlexpert/mlexpert/neural_network.py"
SLIDES = [
 title("Neural Networks", "A multilayer perceptron with backprop", "Neural networks stack simple layers to learn complex functions. In this lecture we build a fully connected network with ReLU and softmax, and derive backpropagation step by step."),
 bullets("The problem", ["Linear models can't learn XOR-like patterns", "Hand-crafting features doesn't scale", "Want the model to learn its own features"],
  "Linear models fail on patterns like XOR, and hand-engineering features doesn't scale. We want a model that learns useful intermediate features by itself."),
 diagram("Architecture", [("input x", "hidden 1 (ReLU)"), ("hidden 1 (ReLU)", "hidden 2 (ReLU)"), ("hidden 2 (ReLU)", "softmax output"), ("softmax output", "cross-entropy loss")],
  "The network is a chain of layers. Each layer multiplies by a weight matrix, adds a bias, and applies a non-linearity: ReLU in hidden layers, softmax at the output, which feeds a cross-entropy loss. Without the non-linearities, the whole stack would collapse into one linear model."),
 eqs("Forward pass", [r"$a_{l+1}=\mathrm{ReLU}(a_lW_l+b_l)$", r"$p=\mathrm{softmax}(a_{L-1}W_{L-1}+b_{L-1})$"], ["He init: W ~ N(0, 2 / fan_in)", "Cache activations for the backward pass"],
  "In the forward pass, each layer's activation feeds the next. Weights start with He initialisation, scaled by two over fan-in, which keeps ReLU signals from vanishing or exploding. We cache every activation because backprop needs them."),
 eqs("Backpropagation", [r"$\delta_L=\frac{p-Y}{n}$", r"$\nabla W_l=a_l^\top\delta_{l},\quad \delta_{l-1}=(\delta_l W_l^\top)\odot[a_l>0]$"], ["Chain rule, layer by layer, from the output back"],
  "Backprop applies the chain rule backwards. With softmax and cross-entropy, the output error is simply probabilities minus one-hot targets. Each weight gradient is the layer's input transposed times its error. The error then flows back through the weights and is masked by where ReLU was active."),
 code("gradients()", src(M, "MLP.gradients"), "Here it is in code. Run forward, subtract one at the true class, divide by batch size, then loop backwards: compute weight and bias gradients, and propagate delta through the weights and the ReLU mask."),
 code("Training loop", src(M, "MLP.fit"), "Training is mini-batch SGD: shuffle each epoch, compute gradients on each batch, and step every weight matrix and bias vector."),
 bullets("Complexity & trade-offs", ["Forward/backward: O(n · Σ layer_in × layer_out)", "Universal approximators, but data hungry", "Needs tuning: lr, depth, width, regularisation", "Tools: dropout, batch norm, Adam, early stopping"],
  "Each pass costs roughly the batch size times the sum of layer weight counts, and backward costs about twice forward. Networks can approximate almost anything, but need lots of data and tuning. Dropout, batch normalisation, Adam, and early stopping are the standard tools."),
 bullets("Recap", ["Layers: linear + non-linearity", "Softmax + cross-entropy → error = p − Y", "Backprop = chain rule backwards", "Train with mini-batch SGD"],
  "To recap: a network stacks linear layers and non-linearities. With softmax and cross-entropy the output error is p minus Y, backprop pushes it backwards with the chain rule, and mini-batch SGD does the learning."),
]
