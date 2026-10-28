# MLExpert · ML System Design

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. ML System Design (0:00) — `slides/01.png`

Machine learning design interviews test whether you can turn a product goal into a working system. This lecture gives a nine-step framework and applies it to five classic prompts.

## 2. The problem (0:10) — `slides/02.png`

You'll get a vague prompt like recommend videos or detect spam, and forty-five minutes to cover data, modelling, serving, and monitoring. A clear structure is what makes the answer land.

## 3. Framework, part 1 (0:22) — `slides/03.png`

Start by turning the product goal into an ML objective, such as predicting click and long watch probability. Define offline and online metrics, plus guardrails. Then data: where labels come from, label delay, class imbalance, leakage, and splitting by time. Then features, kept consistent between training and serving with a feature store.

## 4. Framework, part 2 (0:43) — `slides/04.png`

Next, a simple baseline like logistic regression or boosted trees before deep models. Training choices: loss, negative sampling, tuning. Serving usually has stages: candidate retrieval, ranking, then re-ranking for business rules and diversity, within a latency budget. Roll out with shadow mode and A/B tests, and monitor drift and freshness with a retraining cadence.

## 5. Typical serving stack (1:06) — `slides/05.png`

Here's the typical serving stack. A request triggers fast candidate retrieval, often an approximate nearest-neighbour index over embeddings. A heavier ranking model scores the candidates using features from the feature store. Re-ranking applies rules and diversity, and everything is logged to produce the next training data.

## 6. Video recommendations (1:26) — `slides/06.png`

For video recommendations: retrieve with a two-tower model and an ANN index, plus heuristic sources like subscriptions. Rank with a multi-task model predicting click, watch time, and likes, combined into one score. Handle cold start with content embeddings, popularity priors, and exploration.

## 7. Spam, search, ads, ETA (1:45) — `slides/07.png`

Four more prompts. Spam is highly imbalanced and adversarial: optimise precision at a fixed recall, use a human review queue, and retrain often. Search combines lexical and dense retrieval with learning to rank. Ads need calibrated click probabilities because they feed auctions. ETA prediction regresses on route segments and corrects the routing engine's estimate.

## 8. Recap (2:09) — `slides/08.png`

To recap: go from goal to objective to metrics, think about data and features before models, start with a baseline, serve in stages, and roll out carefully with monitoring and retraining. Deep learning topics like CNNs, RNNs, and GANs are covered in the repo's notes.
