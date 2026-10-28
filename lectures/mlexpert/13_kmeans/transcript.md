# MLExpert · k-Means Clustering

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. k-Means (0:00) — `slides/01.png`

k-means is the go-to clustering algorithm: group unlabeled points into k clusters around centres. We'll cover Lloyd's algorithm and the smarter k-means plus plus initialisation.

## 2. The problem (0:11) — `slides/02.png`

Here there are no labels. We just want to discover groups, say customer segments, where points in a group are close to each other. We decide the number of groups, k, up front.

## 3. Intuition (0:23) — `slides/03.png`

Each cluster is represented by a centre. Every point belongs to its nearest centre, and each centre sits at the mean of its points. Those two conditions define a good clustering.

## 4. Objective and Lloyd's algorithm (0:35) — `slides/04.png`

We minimise the total squared distance to assigned centres, called inertia. Lloyd's algorithm alternates two steps: assign each point to its nearest centre, then move each centre to its points' mean. Each step can only lower inertia, so it converges, though to a local minimum.

## 5. k-means++ initialisation (0:52) — `slides/05.png`

Initialisation matters. k-means plus plus picks the first centre at random, then samples each next centre with probability proportional to the squared distance from the nearest centre chosen so far. Far-away points are likely picks, which spreads the centres out.

## 6. Implementation (1:08) — `slides/06.png`

Here's the code. The init function implements k-means plus plus. Fit alternates predict, which assigns nearest centres, with the mean update, keeping an empty cluster's centre in place, and stops when the largest shift is below a tolerance.

## 7. Complexity & trade-offs (1:23) — `slides/07.png`

Each iteration costs n times k times d. Results depend on initialisation, so run a few seeds and keep the lowest inertia. k-means assumes roughly spherical clusters of similar size, and you choose k with the elbow method or silhouette score.

## 8. Recap (1:37) — `slides/08.png`

To recap: k-means alternates assigning points and updating centres to minimise within-cluster squared distance. Start with k-means plus plus, and you have a fast, simple clustering method.
