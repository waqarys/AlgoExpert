# ML System Design - study notes

## Framework
1. **Clarify the product goal** and translate to an ML objective (e.g. maximise long-term engagement -> predict P(click) and P(dwell > 30s)).
2. **Metrics**: offline (AUC, log loss, NDCG@k, precision@k, RMSE) and online (CTR, retention, revenue, latency); guardrail metrics.
3. **Data**: sources, labels (explicit vs implicit), label delay, class imbalance, leakage, train/validation split by time.
4. **Features**: user, item, context, cross features; embeddings; feature store for train/serve consistency.
5. **Model**: start with a simple baseline (logistic regression / GBDT), then deep models (two-tower, wide & deep, transformers) if justified.
6. **Training**: loss choice, sampling of negatives, regularisation, hyper-parameter search, distributed training.
7. **Serving**: candidate generation -> ranking -> re-ranking (business rules, diversity); latency budgets, caching, batch vs online inference.
8. **Evaluation & rollout**: offline eval, shadow mode, A/B test with power analysis, canary.
9. **Monitoring**: data/prediction drift, feature freshness, model performance decay, retraining cadence, feedback loops.

## Worked prompts
### Recommend videos (YouTube-style)
- Candidates: two-tower retrieval with ANN index (user tower: history embeddings; item tower: content + metadata) plus heuristics (subscriptions, trending).
- Ranking: multi-task model predicting click, watch time, like; final score = weighted combination.
- Cold start: content embeddings, popularity priors, exploration (bandits).
### Spam / abuse detection
- Highly imbalanced; optimise precision at fixed recall; human review queue for borderline; adversarial drift -> frequent retraining; graph features (account networks).
### Search ranking
- Query understanding (spell correction, intent), retrieval (BM25 + dense), learning-to-rank (LambdaMART / neural) with NDCG; position-bias correction from click logs.
### Ad click prediction
- Calibrated probabilities matter (used in auctions); logistic regression / FM / DLRM on sparse features with hashing; log loss + calibration plots; near-real-time updates.
### ETA prediction (ride-hailing)
- Regression on route segments, traffic, time-of-day; MAE/percentile error; GBDT or graph neural nets; residual correction of routing-engine estimate.

## Fundamentals checklist (covered in code in `mlexpert/`)
| Topic | Module |
|---|---|
| Linear / ridge regression (closed form + GD) | `linear_regression.py` |
| Logistic & softmax regression | `logistic_regression.py` |
| Gradient descent, SGD, momentum, Adam | `optimizers.py` |
| k-NN | `knn.py` |
| k-means (k-means++) | `kmeans.py` |
| Decision tree (CART), random forest | `decision_tree.py` |
| Gaussian naive Bayes | `naive_bayes.py` |
| PCA | `pca.py` |
| MLP with backprop | `neural_network.py` |
| Metrics (accuracy, P/R/F1, ROC-AUC, log loss, MSE, R²) | `metrics.py` |
| Scaling, one-hot, splits, k-fold | `preprocessing.py` |

## Concepts to be able to explain
Bias-variance trade-off, regularisation (L1 vs L2), overfitting & cross-validation, class imbalance (resampling, class weights, focal loss), vanishing gradients, batch norm, dropout, embeddings, bagging vs boosting, precision/recall trade-off, calibration, A/B testing statistics.

## MLExpert course design questions (real question names, my own notes)
### Design a machine learning platform
Feature store (offline in a warehouse, online in a KV store, with point-in-time joins), training orchestration (pipelines, GPU scheduling), experiment tracking and model registry, batch and online serving, shadow and A/B deploys, monitoring for data drift and prediction drift, retraining triggers.
### Design Facebook photo tagging
Face detection (CNN detector) → face embedding (metric learning, triplet/ArcFace loss) → match against the embeddings of the uploader's friends (ANN index), with a confidence threshold. Privacy opt-in. Users confirming or rejecting suggestions provides labels. Metrics: precision@1, coverage.
### Design Amazon Alexa
Wake word on device (small CNN/RNN) → streaming ASR → NLU (intent classification + slot filling) → skill routing/dialog manager → TTS. Latency budget under ~1 s. Train on reviewed failure cases; measure WER and intent accuracy.
### Design a fake news detector
Signals: text (transformer classifier), source reputation, propagation graph (who shares, how fast), user reports. Human fact-checkers in the loop. Act by down-ranking rather than deleting. Labels are scarce and adversarial, so use active learning and monitor drift.
### Design YouTube's recommendation system
Two stages: candidate generation (two-tower embeddings + ANN; collaborative signals) then ranking (deep model predicting watch time, CTR and satisfaction), then re-ranking for diversity and freshness. Avoid clickbait by using watch time and surveys. Handle cold start with content features.

## Deep learning lessons (theory)
- **CNNs:** convolution = shared local weights; pooling; receptive field; ResNet skip connections.
- **RNNs:** hidden state over time; vanishing gradients → LSTM/GRU gates; now mostly replaced by Transformers (attention).
- **GANs:** generator vs discriminator minimax; mode collapse; WGAN; evaluate with FID.
