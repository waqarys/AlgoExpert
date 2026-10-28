# MLExpert · Singular Value Decomposition

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Singular Value Decomposition (0:00) — `slides/01.png`

The singular value decomposition underpins PCA, recommenders, and compression. Here we build a truncated SVD from scratch using power iteration and deflation.

## 2. The problem (0:11) — `slides/02.png`

We have a big matrix, like users by items, and want its best low-rank approximation, keeping only the top k patterns, without paying for a full decomposition.

## 3. SVD (0:21) — `slides/03.png`

Any matrix is a sum of rank-one pieces, each a singular value times an outer product of left and right singular vectors. Keeping the k largest terms gives the best rank-k approximation, a result known as Eckart-Young.

## 4. Power iteration (0:34) — `slides/04.png`

To find the top piece, use power iteration. Multiply a random vector by A transpose A and normalise, again and again. The component along the dominant direction grows fastest, so v converges to the top right singular vector. Then sigma is the length of A v, and u is A v divided by sigma.

## 5. Deflation (0:54) — `slides/05.png`

To get the next component, deflate: subtract the found rank-one piece from the matrix, and run power iteration again on what's left. After k rounds we have the top k singular triples.

## 6. truncated_svd (1:05) — `slides/06.png`

Here's the full function. For each of k components: random start, iterate with A transpose A on the residual, compute sigma and u, store them, and deflate.

## 7. Complexity & trade-offs (1:16) — `slides/07.png`

Cost is k times iterations times the matrix size, great when k is small. Convergence slows when consecutive singular values are close, and small errors accumulate through deflation. In production, randomized SVD or Lanczos methods are the standard.

## 8. Recap (1:33) — `slides/08.png`

To recap: SVD writes a matrix as a sum of ranked pieces. Power iteration finds the top one, deflation exposes the next, and this is the engine behind PCA, latent semantic analysis, and recommenders.
