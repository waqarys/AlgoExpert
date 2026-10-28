# MLExpert - from-scratch ML in Python

numpy-only implementations of the classic ML interview algorithms, with pytest tests, plus ML system design notes (`ml_design_notes.md`).

```bash
cd mlexpert
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Coverage vs. the MLExpert Machine Learning Crash Course (18 lessons)
| Lesson | Code |
|---|---|
| Naive Bayes / Performance / NB Optimizations | `naive_bayes.py` (Gaussian), `multinomial_nb.py` (Laplace smoothing, log space), `metrics.py` |
| K Nearest Neighbors | `knn.py` |
| Decision Trees | `decision_tree.py` (CART + random forest), `gradient_boosting.py` |
| Linear Regression | `linear_regression.py`, `regularization.py` (ridge, lasso, elastic net) |
| Logistic Regression | `logistic_regression.py` (binary + softmax) |
| Support Vector Machine | `svm.py` (linear SVM, Pegasos / hinge loss) |
| K-means | `kmeans.py` (k-means++) |
| Singular Value Decomposition | `svd.py` (power iteration), `pca.py` |
| Neural Networks | `neural_network.py` (MLP + backprop), `optimizers.py` |
| CNNs / RNNs / GANs | theory only; see `ml_design_notes.md` |
| Collaborative and Content Based Filtering | `recommender.py` (ALS matrix factorisation, cosine content similarity) |
| Learning To Rank | `learning_to_rank.py` (NDCG, pairwise RankNet-style ranker) |
| Model evaluation | `model_selection.py` (k-fold `cross_val_score`, bias-variance decomposition demo) |

The lesson list comes from the public course outline. The ML design questions in the course are: ML platform, Facebook photo tagging, Amazon Alexa, fake news detector, and YouTube recommendations.
