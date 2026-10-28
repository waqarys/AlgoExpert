from speclib import *
TITLE = "MLExpert · Data Preprocessing"; OUT = "mlexpert/01_preprocessing"; M = "mlexpert/mlexpert/preprocessing.py"
SLIDES = [
 title("Data Preprocessing", "Scaling, encoding and honest splits", "Before any model learns anything, the data has to be shaped correctly. In this lecture we cover four small utilities that every ML pipeline needs: standard scaling, one-hot encoding, a train-test split, and k-fold indices."),
 bullets("The problem", ["Features live on wildly different scales", "Models need numbers, not category labels", "We must measure performance on unseen data"],
  "Three problems show up in almost every dataset. Features have different scales, like age in tens and income in thousands. Categories such as colour aren't numbers. And if we evaluate on the data we trained on, we fool ourselves."),
 eqs("Standard scaling", [r"$z = \frac{x - \mu}{\sigma}$"], ["Fit μ and σ on the training set only", "A constant column gets σ = 1 to avoid ÷0", "Helps gradient descent, k-NN, SVM, PCA"],
  "Standard scaling subtracts each column's mean and divides by its standard deviation, so every feature is centred at zero with unit spread. Crucially, the mean and deviation are learned from training data only, then reused on test data. A constant column would divide by zero, so we set its deviation to one."),
 code("StandardScaler", src(M, "StandardScaler"), "Here's the scaler. Fit stores the column means and deviations, patching zeros. Transform simply applies the formula. Splitting fit from transform is what prevents test data leaking into training."),
 bullets("One-hot encoding", ["Class 2 of 4  →  [0, 0, 1, 0]", "No fake ordering between categories", "Also the target format for softmax"],
  "One-hot encoding turns a category index into a vector with a single one. Class two of four becomes zero, zero, one, zero. This avoids implying that category three is somehow bigger than category one, and it's exactly the target format a softmax classifier expects."),
 code("one_hot", src(M, "one_hot"), "The implementation allocates a zero matrix and uses fancy indexing to drop a one into each row at the label's column, in a single vectorised step."),
 bullets("Honest evaluation", ["Shuffle, then cut: train 75% / test 25%", "k-fold: every point validates exactly once", "Fixed seed → reproducible experiments"],
  "For evaluation we shuffle the indices and cut them into training and test parts. K-fold goes further: split into k folds, and let each fold take a turn as the validation set while the rest train. Every example is validated exactly once, and a fixed seed keeps results reproducible."),
 code("Split and k-fold", src(M, "train_test_split", "k_fold_indices"), "Both helpers start from a seeded permutation. The split cuts it at the right fraction; k-fold uses array split and pairs each fold with the concatenation of all the others."),
 bullets("Recap", ["Scale with training statistics only", "One-hot for categories", "Shuffle + split, or k-fold, for honest scores", "All operations are O(n·d)"],
  "To recap: scale using training statistics only, one-hot encode categories, and always evaluate on held-out data, with a single split or k-fold. Each of these is linear in the size of the data, so they're cheap, but getting them wrong silently ruins results."),
]
