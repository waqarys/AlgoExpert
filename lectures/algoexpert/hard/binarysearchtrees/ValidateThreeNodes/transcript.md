# AlgoExpert · Validate Three Nodes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Three Nodes (0:00) — `slides/01.png`

Let's solve Validate Three Nodes, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Is nodeTwo a descendant of one of nodeOne or nodeThree and an ancestor of the other?

## 3. Intuition (0:19) — `slides/03.png`

Node two must sit on the path between the other two, so search down from node one and node three.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Instead of exploring the whole tree, we can use BST searches: check whether one reaches two, then two reaches three, or the other way around. That's height time.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, check if node two descends from node one or node three. Second, then check that the other one descends from node two. Third, use BST search for each step.

## 6. Worked example (0:49) — `slides/06.png`

Is two between five and three: is five an ancestor of two, and two an ancestor of three, or the reverse?

## 7. Worked example (0:56) — `slides/07.png`

Starting at five, search for two using BST order: go left, found it. So five is an ancestor of two.

## 8. Worked example (1:04) — `slides/08.png`

Now search for three from two: right to four, left to three. Found, so the answer is true.

## 9. Java solution (1:12) — `slides/09.png`

If two descends from one, return whether three descends from two. Otherwise if two descends from three, return whether one descends from two. Descends walks down using BST order until it hits the target or null.

## 10. Complexity (1:26) — `slides/10.png`

Time is O of h. Space is constant.

## 11. Edge cases & pitfalls (1:30) — `slides/11.png`

Check both directions, and compare node references, not just values.

## 12. Interview tips & follow-ups (1:35) — `slides/12.png`

Mention the optimisation that searches from both ends at once, stopping early.

## 13. Recap (1:40) — `slides/13.png`

To recap Validate Three Nodes: Node two must sit on the path between the other two, so search down from node one and node three. Try re-implementing it from scratch without looking.
