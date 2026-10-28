# MLExpert · Recommender Systems

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Recommender Systems (0:00) — `slides/01.png`

Recommenders decide what you watch, read, and buy. We'll build collaborative filtering with matrix factorisation, and content-based similarity, from scratch.

## 2. The problem (0:10) — `slides/02.png`

We have a users by items matrix of ratings, and almost all of it is missing. The task is to predict the missing entries and recommend each user's top predicted items.

## 3. Matrix factorisation (0:21) — `slides/03.png`

Collaborative filtering by matrix factorisation gives every user and every item a short vector of k hidden factors. A predicted rating is the dot product of the two. Factors might come to mean things like action versus romance, learned purely from ratings.

## 4. Alternating least squares (0:37) — `slides/04.png`

Solving for P and Q together is hard, but if we fix the item vectors, each user's vector is just a small ridge regression on the items they rated. Then fix users and solve for items. Alternating between them is ALS, and each step can only lower the loss.

## 5. ALS (0:53) — `slides/05.png`

The code builds a mask of observed entries, initialises small random factors, then alternates: for each user, solve a k by k system using only the items they rated, then the same for each item.

## 6. Content-based filtering (1:05) — `slides/06.png`

Content-based filtering instead describes items by features, like genre or tags, and recommends items similar to what the user already liked, using cosine similarity. It works for brand-new items that have no ratings yet.

## 7. Cosine similarity (1:19) — `slides/07.png`

Normalise each item's feature vector to unit length, guarding zero vectors, and one matrix product gives all pairwise cosine similarities.

## 8. Trade-offs (1:27) — `slides/08.png`

ALS costs a small k by k solve per user and item each iteration, and parallelises well. Collaborative filtering struggles with new users and items; content-based methods lack novelty. Real systems are hybrids, often with a fast retrieval stage followed by a ranking model.

## 9. Recap (1:45) — `slides/09.png`

To recap: model ratings as user times item factors, fit them with alternating ridge regressions, use content similarity for cold start, and combine both in practice.
