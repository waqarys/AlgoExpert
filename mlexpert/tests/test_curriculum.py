import numpy as np
import pytest

from mlexpert.gradient_boosting import GradientBoostingRegressor, RegressionTree
from mlexpert.learning_to_rank import PairwiseRanker, dcg, ndcg
from mlexpert.linear_regression import LinearRegression
from mlexpert.logistic_regression import LogisticRegression
from mlexpert.model_selection import bias_variance, cross_val_score, polynomial_features
from mlexpert.multinomial_nb import MultinomialNB
from mlexpert.recommender import MatrixFactorization, content_similarity
from mlexpert.regularization import ElasticNet, Lasso, Ridge, soft_threshold
from mlexpert.svd import truncated_svd
from mlexpert.svm import LinearSVM

rng = np.random.default_rng(7)


def two_blobs(n=50, gap=4.0):
    X = np.vstack([rng.normal(0, 0.6, (n, 2)), rng.normal(gap, 0.6, (n, 2))])
    return X, np.r_[np.zeros(n, int), np.ones(n, int)]


# ---- k-fold cross-validation ----
def test_cross_val_score_k_scores_and_high_accuracy():
    X, y = two_blobs()
    s = cross_val_score(lambda: LogisticRegression(), X, y, k=5)
    assert s.shape == (5,) and s.mean() > 0.95


def test_cross_val_score_custom_metric_and_bad_k():
    X = rng.normal(size=(40, 1)); y = 3 * X[:, 0] + 1
    s = cross_val_score(lambda: LinearRegression(), X, y, k=4, score=lambda t, p: -np.mean((t - p) ** 2))
    assert np.all(s > -1e-9)
    with pytest.raises(ValueError):
        cross_val_score(lambda: LinearRegression(), X, y, k=1)
    with pytest.raises(ValueError):
        cross_val_score(lambda: LinearRegression(), X, y, k=41)


# ---- SVM ----
def test_linear_svm_separates_blobs():
    X, y = two_blobs()
    m = LinearSVM(lam=0.01, epochs=30).fit(X, y)
    assert np.mean(m.predict(X) == y) > 0.97
    assert m.hinge_loss(X, y) < 0.5


def test_linear_svm_accepts_pm1_labels_and_margin_sign():
    X = np.array([[-2.0], [-1.0], [1.0], [2.0]]); y = np.array([-1, -1, 1, 1])
    m = LinearSVM(lam=0.01, epochs=200).fit(X, y)
    assert list(m.predict(X)) == [0, 0, 1, 1]
    assert m.decision_function([[3.0]])[0] > 1 and m.decision_function([[-3.0]])[0] < -1


# ---- gradient boosting ----
def test_regression_tree_step_function():
    X = np.arange(10).reshape(-1, 1); y = np.where(X[:, 0] < 5, 1.0, 3.0)
    assert np.allclose(RegressionTree(max_depth=1).fit(X, y).predict(X), y)


def test_regression_tree_constant_target_is_leaf():
    t = RegressionTree().fit(np.ones((5, 1)), np.full(5, 2.0))
    assert t.root == 2.0


def test_gradient_boosting_fits_sine_and_loss_decreases():
    X = np.linspace(0, 6, 200).reshape(-1, 1); y = np.sin(X[:, 0])
    m = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3).fit(X, y)
    assert np.mean((m.predict(X) - y) ** 2) < 0.01
    assert all(a >= b - 1e-12 for a, b in zip(m.train_loss_, m.train_loss_[1:]))


def test_gradient_boosting_zero_estimators_predicts_mean():
    X = np.arange(4).reshape(-1, 1); y = np.array([1.0, 2, 3, 6])
    assert np.allclose(GradientBoostingRegressor(n_estimators=0).fit(X, y).predict(X), 3.0)


# ---- regularization ----
def test_soft_threshold():
    assert np.allclose(soft_threshold(np.array([-3.0, 0.5, 2.0]), 1.0), [-2.0, 0.0, 1.0])


def test_lasso_zeroes_irrelevant_features():
    X = rng.normal(size=(200, 5)); y = 4 * X[:, 0] - 2 * X[:, 1] + rng.normal(0, 0.1, 200)
    w = Lasso(alpha=0.1).fit(X, y).w
    assert abs(w[0] - 4) < 0.3 and abs(w[1] + 2) < 0.3
    assert np.all(np.abs(w[2:]) < 1e-8)


def test_ridge_shrinks_and_matches_ols_at_zero():
    X = rng.normal(size=(100, 3)); y = X @ np.array([1.0, -2.0, 3.0]) + 0.5
    ols = LinearRegression().fit(X, y)
    assert np.allclose(Ridge(alpha=0.0).fit(X, y).w, ols.w)
    assert np.linalg.norm(Ridge(alpha=100).fit(X, y).w) < np.linalg.norm(ols.w)


def test_elastic_net_between_lasso_and_ridge_and_huge_alpha_gives_zero():
    X = rng.normal(size=(100, 3)); y = X @ np.array([1.0, 0.0, 2.0])
    assert np.allclose(ElasticNet(alpha=1e6).fit(X, y).w, 0)
    w = ElasticNet(alpha=0.1, l1_ratio=0.5).fit(X, y).w
    assert abs(w[1]) < 0.05 and w[2] > w[0] > 0


# ---- bias-variance ----
def test_bias_variance_tradeoff_with_polynomial_degree():
    f = lambda x: np.sin(2 * np.pi * x)
    make = lambda: LinearRegression()
    b1, v1, _ = bias_variance(make, f, degree=1, n_sets=100)
    b9, v9, n2 = bias_variance(make, f, degree=9, n_sets=100)
    assert b1 > b9, "simple model has more bias"
    assert v9 > v1, "complex model has more variance"
    assert n2 == pytest.approx(0.09)


def test_polynomial_features_shape():
    assert polynomial_features([1, 2], 3).tolist() == [[1, 1, 1], [2, 4, 8]]


# ---- SVD ----
def test_truncated_svd_matches_numpy():
    A = rng.normal(size=(6, 4))
    U, S, V = truncated_svd(A, 2)
    assert np.allclose(S, np.linalg.svd(A, compute_uv=False)[:2], atol=1e-6)
    assert np.allclose(np.abs(U.T @ U), np.eye(2), atol=1e-6)


def test_truncated_svd_rank_one_reconstruction_and_zero_matrix():
    A = np.outer([1.0, 2, 3], [1.0, 0, -1])
    U, S, V = truncated_svd(A, 1)
    assert np.allclose(S[0] * np.outer(U[:, 0], V[0]), A)
    assert truncated_svd(np.zeros((3, 3)), 1)[1][0] == 0


# ---- recommender ----
def test_matrix_factorization_recovers_missing_entry():
    P, Q = rng.normal(size=(8, 2)), rng.normal(size=(6, 2))
    R = P @ Q.T
    obs = R.copy(); obs[0, 0] = np.nan
    m = MatrixFactorization(k=2, reg=1e-3, iters=200).fit(obs)
    assert abs(m.predict()[0, 0] - R[0, 0]) < 0.1


def test_content_similarity_handles_zero_vector():
    S = content_similarity([[1, 0], [1, 1], [0, 0]])
    assert S[0, 0] == pytest.approx(1) and S[0, 1] == pytest.approx(1 / np.sqrt(2)) and S[2, 2] == 0


# ---- learning to rank ----
def test_ndcg_perfect_worst_and_empty():
    assert ndcg([3, 2, 1, 0]) == pytest.approx(1)
    assert ndcg([0, 1, 2, 3]) < 0.7
    assert ndcg([0, 0]) == 0.0
    assert dcg([3], k=1) == pytest.approx(7)


def test_pairwise_ranker_learns_relevance_order():
    X = rng.normal(size=(60, 3)); rel = (X @ np.array([2.0, -1.0, 0.0]) > 0).astype(int) + (X[:, 0] > 1)
    qid = np.repeat(np.arange(6), 10)
    m = PairwiseRanker(epochs=300).fit(X, rel, qid)
    scores = [ndcg(rel[qid == q][np.argsort(-m.score(X[qid == q]))]) for q in range(6)]
    assert np.mean(scores) > 0.9


def test_pairwise_ranker_no_pairs():
    assert np.all(PairwiseRanker().fit(np.ones((3, 2)), [1, 1, 1], [0, 0, 0]).w == 0)


# ---- multinomial naive Bayes ----
def test_multinomial_nb_spam():
    # vocab: [free, money, meeting, report]
    X = np.array([[3, 2, 0, 0], [2, 3, 0, 1], [0, 0, 2, 3], [0, 1, 3, 2]]); y = np.array(["spam", "spam", "ham", "ham"])
    m = MultinomialNB().fit(X, y)
    assert list(m.predict([[4, 1, 0, 0], [0, 0, 1, 4]])) == ["spam", "ham"]
    assert np.all(np.isfinite(m.log_likelihood_)), "smoothing avoids log(0)"
