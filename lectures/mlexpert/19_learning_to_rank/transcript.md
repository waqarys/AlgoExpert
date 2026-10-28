# MLExpert · Learning to Rank

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Learning to Rank (0:00) — `slides/01.png`

Search engines and feeds don't need exact scores; they need the right order. This lecture covers the NDCG metric and a pairwise, RankNet-style ranker.

## 2. The problem (0:10) — `slides/02.png`

For each query we have candidate documents with graded relevance. We want to order them so the most relevant appear first, because users rarely look past the top few results.

## 3. DCG and NDCG (0:21) — `slides/03.png`

DCG rewards relevant documents, with gains that grow exponentially in relevance, and discounts them by the log of their position. Dividing by the DCG of the ideal ordering gives NDCG, between zero and one.

## 4. NDCG (0:35) — `slides/04.png`

The code is a direct translation: compute gains and log discounts for the first k items, and divide by the DCG of the sorted, ideal list.

## 5. Pairwise approach (0:43) — `slides/05.png`

Directly optimising NDCG is hard because sorting isn't differentiable. The pairwise trick: for every pair in the same query where i is more relevant than j, we want i's score higher. A logistic loss on the score difference does that, as in RankNet.

## 6. PairwiseRanker.fit (0:59) — `slides/06.png`

The ranker builds all valid pairs within each query, takes feature differences, and runs gradient ascent on the log-likelihood that the more relevant item wins. Scores are a linear model, X times w.

## 7. Trade-offs (1:11) — `slides/07.png`

There are three families. Pointwise regresses relevance directly but ignores ordering. Pairwise, like ours, learns order but has quadratic pairs per query. Listwise methods like LambdaMART optimise NDCG-style objectives. With click data, always correct for position bias.

## 8. Recap (1:31) — `slides/08.png`

To recap: evaluate rankings with NDCG at k, train a pairwise ranker with logistic loss on score differences within each query, and reach for listwise methods in production.
