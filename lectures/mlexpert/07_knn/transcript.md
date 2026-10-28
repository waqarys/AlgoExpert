# MLExpert · k-Nearest Neighbours

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. k-Nearest Neighbours (0:00) — `slides/01.png`

k-nearest neighbours may be the simplest model there is: no training at all, just memory and a distance function. Let's see how it works, how to code it, and where it breaks.

## 2. The problem (0:10) — `slides/02.png`

We want to label a new point, without assuming a linear boundary or any particular form. The only assumption is that similar inputs have similar outputs.

## 3. Intuition (0:20) — `slides/03.png`

So, to label the yellow star, find its k closest training points. For classification, take a majority vote of their labels. For regression, average their values. That's the whole algorithm.

## 4. Distance (0:34) — `slides/04.png`

We use Euclidean distance, so feature scaling is essential, otherwise the feature with the biggest units dominates. Choose k by cross-validation: small k follows noise, large k blurs the boundary. An odd k avoids ties in two-class problems.

## 5. Implementation (0:50) — `slides/05.png`

Fit just stores the data. Predict computes all pairwise squared distances with broadcasting, takes the k smallest with argsort, and either averages the neighbours' values or picks the most common label.

## 6. Complexity & trade-offs (1:02) — `slides/06.png`

Training is free, but each prediction scans all n points, so it's order n times d per query, and the whole dataset sits in memory. In high dimensions all distances look similar, which hurts accuracy. KD-trees or approximate nearest-neighbour indexes speed things up.

## 7. Recap (1:19) — `slides/07.png`

To recap: k-NN stores the data and votes or averages at query time. Scale features and tune k. It's cheap to train but expensive to query, and a solid baseline in low dimensions.
