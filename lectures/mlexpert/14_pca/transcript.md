# MLExpert · Principal Component Analysis

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. PCA (0:00) — `slides/01.png`

Principal component analysis compresses data into fewer dimensions while keeping as much variation as possible. We'll see the geometry and a clean implementation using SVD.

## 2. The problem (0:11) — `slides/02.png`

Datasets often have hundreds of correlated features. They're hard to visualise and slow to model. We'd like a few new features that keep most of the information.

## 3. Intuition: directions of spread (0:22) — `slides/03.png`

Look at this cloud. The pink arrow points along the direction of greatest spread: the first principal component. The second is perpendicular and captures what's left. Projecting onto the top few components keeps the shape while dropping dimensions.

## 4. Via SVD (0:38) — `slides/04.png`

Centre the data and take its singular value decomposition. The rows of V transpose are the principal directions, sorted by singular value. Each component's variance is its singular value squared over n minus one, which gives the explained variance ratio.

## 5. PCA (0:55) — `slides/05.png`

The implementation centres, calls SVD with thin matrices, keeps the top components, and computes the explained variance ratio. Transform projects onto the components, and inverse transform maps back, giving a reconstruction.

## 6. Complexity & trade-offs (1:09) — `slides/06.png`

A thin SVD costs n times d times the smaller of n and d. Scale features first, otherwise large-unit features dominate. PCA is linear, and components mix features so they can be hard to interpret. A common rule is to keep enough components for ninety-five percent of the variance.

## 7. Recap (1:26) — `slides/07.png`

To recap: centre the data, run SVD, and keep the top k directions. They're orthogonal and ordered by variance, useful for compression, visualisation, and denoising.
