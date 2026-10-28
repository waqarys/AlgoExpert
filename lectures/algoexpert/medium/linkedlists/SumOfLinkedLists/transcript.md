# AlgoExpert · Sum Of Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sum Of Linked Lists (0:00) — `slides/01.png`

Let's solve Sum Of Linked Lists, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Lists store digits least-significant first; return their sum in the same format.

## 3. Intuition (0:19) — `slides/03.png`

Add digit by digit like grade school, carrying into the next node.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, walk both lists together. Second, sum digits plus carry. Third, create a node with the ones digit. Fourth, carry the rest.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with sum of linked lists. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of max(n, m). Space is O of max(n, m).

## 7. Recap (0:51) — `slides/07.png`

To recap Sum Of Linked Lists: Add digit by digit like grade school, carrying into the next node. Try re-implementing it from scratch without looking.
