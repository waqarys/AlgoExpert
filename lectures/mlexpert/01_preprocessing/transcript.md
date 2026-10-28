# MLExpert · Data Preprocessing

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Data Preprocessing (0:00) — `slides/01.png`

Before any model learns anything, the data has to be shaped correctly. In this lecture we cover four small utilities that every ML pipeline needs: standard scaling, one-hot encoding, a train-test split, and k-fold indices.

## 2. The problem (0:13) — `slides/02.png`

Three problems show up in almost every dataset. Features have different scales, like age in tens and income in thousands. Categories such as colour aren't numbers. And if we evaluate on the data we trained on, we fool ourselves.

## 3. Standard scaling (0:29) — `slides/03.png`

Standard scaling subtracts each column's mean and divides by its standard deviation, so every feature is centred at zero with unit spread. Crucially, the mean and deviation are learned from training data only, then reused on test data. A constant column would divide by zero, so we set its deviation to one.

## 4. StandardScaler (0:48) — `slides/04.png`

Here's the scaler. Fit stores the column means and deviations, patching zeros. Transform simply applies the formula. Splitting fit from transform is what prevents test data leaking into training.

## 5. One-hot encoding (1:02) — `slides/05.png`

One-hot encoding turns a category index into a vector with a single one. Class two of four becomes zero, zero, one, zero. This avoids implying that category three is somehow bigger than category one, and it's exactly the target format a softmax classifier expects.

## 6. one_hot (1:19) — `slides/06.png`

The implementation allocates a zero matrix and uses fancy indexing to drop a one into each row at the label's column, in a single vectorised step.

## 7. Honest evaluation (1:28) — `slides/07.png`

For evaluation we shuffle the indices and cut them into training and test parts. K-fold goes further: split into k folds, and let each fold take a turn as the validation set while the rest train. Every example is validated exactly once, and a fixed seed keeps results reproducible.

## 8. Split and k-fold (1:46) — `slides/08.png`

Both helpers start from a seeded permutation. The split cuts it at the right fraction; k-fold uses array split and pairs each fold with the concatenation of all the others.

## 9. Recap (1:56) — `slides/09.png`

To recap: scale using training statistics only, one-hot encode categories, and always evaluate on held-out data, with a single split or k-fold. Each of these is linear in the size of the data, so they're cheap, but getting them wrong silently ruins results.
