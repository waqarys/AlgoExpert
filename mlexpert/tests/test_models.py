import numpy as np
import pytest

from mlexpert import metrics, optimizers
from mlexpert.decision_tree import DecisionTree, RandomForest, entropy, gini
from mlexpert.kmeans import KMeans
from mlexpert.knn import KNN
from mlexpert.linear_regression import LinearRegression
from mlexpert.logistic_regression import LogisticRegression, SoftmaxRegression
from mlexpert.naive_bayes import GaussianNB
from mlexpert.neural_network import MLP
from mlexpert.pca import PCA
from mlexpert.preprocessing import StandardScaler, k_fold_indices, one_hot, train_test_split

rng = np.random.default_rng(42)


def blobs(n=60):
    a = rng.normal([0, 0], 0.5, (n, 2))
    b = rng.normal([4, 4], 0.5, (n, 2))
    return np.vstack([a, b]), np.array([0] * n + [1] * n)


def test_metrics():
    y, p = [1, 0, 1, 1, 0], [1, 0, 0, 1, 1]
    assert metrics.accuracy(y, p) == 0.6
    assert metrics.confusion_matrix(y, p).tolist() == [[1, 1], [1, 2]]
    pr, rc, f1 = metrics.precision_recall_f1(y, p)
    assert pr == pytest.approx(2 / 3) and rc == pytest.approx(2 / 3) and f1 == pytest.approx(2 / 3)
    assert metrics.roc_auc([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8]) == pytest.approx(0.75)
    assert metrics.log_loss([1, 0], [0.9, 0.1]) == pytest.approx(-np.log(0.9))
    assert metrics.mse([1, 2], [1, 4]) == 2
    assert metrics.r2_score([1, 2, 3], [1, 2, 3]) == 1


def test_linear_regression_closed_form_and_gd():
    X = rng.normal(size=(100, 2))
    y = X @ np.array([3.0, -2.0]) + 5
    m = LinearRegression().fit(X, y)
    assert np.allclose(m.w, [3, -2]) and m.b == pytest.approx(5)
    g = LinearRegression(method="gd", lr=0.1, epochs=2000).fit(X, y)
    assert np.allclose(g.w, [3, -2], atol=1e-3)
    ridge = LinearRegression(l2=100).fit(X, y)
    assert np.linalg.norm(ridge.w) < np.linalg.norm(m.w)


def test_optimizers_converge():
    X = np.hstack([rng.normal(size=(200, 1)), np.ones((200, 1))])
    y = X @ np.array([2.0, 1.0])
    for opt in (optimizers.batch_gd, optimizers.minibatch_sgd, optimizers.adam):
        w = opt(optimizers.mse_grad, np.zeros(2), X, y)
        assert np.allclose(w, [2, 1], atol=0.05), opt.__name__
    w = optimizers.momentum_gd(optimizers.mse_grad, np.zeros(2), X, y, lr=0.05)
    assert np.allclose(w, [2, 1], atol=0.05)


def test_logistic_and_softmax():
    X, y = blobs()
    m = LogisticRegression().fit(X, y)
    assert metrics.accuracy(y, m.predict(X)) > 0.97
    assert m.predict_proba([[4, 4]])[0] > 0.9
    X3 = np.vstack([X, rng.normal([0, 4], 0.5, (60, 2))])
    y3 = np.concatenate([y, [2] * 60])
    s = SoftmaxRegression().fit(X3, y3)
    assert metrics.accuracy(y3, s.predict(X3)) > 0.95


def test_knn():
    X, y = blobs()
    assert KNN(3).fit(X, y).predict([[0, 0], [4, 4]]).tolist() == [0, 1]
    r = KNN(2, task="regression").fit([[0], [1], [10]], [0, 2, 100])
    assert r.predict([[0.4]])[0] == pytest.approx(1)


def test_kmeans():
    X, y = blobs()
    km = KMeans(2).fit(X)
    acc = metrics.accuracy(y, km.labels_)
    assert max(acc, 1 - acc) > 0.98  # cluster ids are arbitrary
    assert km.inertia_ < 100


def test_decision_tree_and_forest():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]] * 10, float)
    y = np.array([0, 1, 1, 0] * 10)  # XOR needs depth 2
    assert metrics.accuracy(y, DecisionTree(max_depth=3).fit(X, y).predict(X)) == 1.0
    assert gini([1, 1]) == 0 and entropy([0, 1]) == pytest.approx(1)
    Xb, yb = blobs()
    assert metrics.accuracy(yb, RandomForest(n_trees=10).fit(Xb, yb).predict(Xb)) > 0.97


def test_naive_bayes():
    X, y = blobs()
    assert metrics.accuracy(y, GaussianNB().fit(X, y).predict(X)) > 0.97


def test_pca():
    t = rng.normal(size=200)
    X = np.c_[t, 2 * t + rng.normal(0, 0.01, 200), rng.normal(0, 0.01, 200)]
    p = PCA(1).fit(X)
    assert p.explained_variance_ratio_[0] > 0.99
    assert np.allclose(p.inverse_transform(p.transform(X)), X, atol=0.1)


def test_mlp_backprop_gradient_check_and_xor():
    net = MLP([2, 4, 2], seed=1)
    X = rng.normal(size=(5, 2))
    y = np.array([0, 1, 1, 0, 1])
    gW, _ = net.gradients(X, y)
    eps = 1e-5
    net.W[0][0, 0] += eps
    lp = net.loss(X, y)
    net.W[0][0, 0] -= 2 * eps
    lm = net.loss(X, y)
    net.W[0][0, 0] += eps
    assert gW[0][0, 0] == pytest.approx((lp - lm) / (2 * eps), rel=1e-4, abs=1e-7)
    Xx = np.array([[0, 0], [0, 1], [1, 0], [1, 1]] * 25, float)
    yx = np.array([0, 1, 1, 0] * 25)
    m = MLP([2, 16, 2], lr=0.2, epochs=300, seed=0).fit(Xx, yx)
    assert metrics.accuracy(yx, m.predict(Xx)) == 1.0


def test_preprocessing():
    Z = StandardScaler().fit(np.array([[1.0, 5], [3, 5]])).transform([[1, 5], [3, 5]])
    assert np.allclose(Z, [[-1, 0], [1, 0]])
    assert one_hot([0, 2]).tolist() == [[1, 0, 0], [0, 0, 1]]
    X, y = np.arange(20).reshape(10, 2), np.arange(10)
    a, b, c, d = train_test_split(X, y, 0.3)
    assert len(a) == 7 and len(b) == 3
    folds = k_fold_indices(10, 5)
    assert len(folds) == 5 and all(len(te) == 2 for _, te in folds)
