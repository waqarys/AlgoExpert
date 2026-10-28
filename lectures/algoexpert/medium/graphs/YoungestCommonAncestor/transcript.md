# AlgoExpert · Youngest Common Ancestor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Youngest Common Ancestor (0:00) — `slides/01.png`

Let's solve Youngest Common Ancestor, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Nodes have only an ancestor pointer; find the deepest common ancestor of two descendants. Equalise depths, then walk up together.

## 3. Intuition (0:22) — `slides/03.png`

Bring both descendants to the same depth, then climb together until they meet.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

One approach stores all of one node's ancestors in a set, then walks up from the other until it finds one. Equalising depths and then climbing both in lockstep avoids extra memory.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, compute both depths. Second, lift the deeper one. Third, move both up until equal.

## 6. Worked example (0:49) — `slides/06.png`

Find the youngest common ancestor of E and I. E is at depth two, I at depth three.

## 7. Worked example (0:55) — `slides/07.png`

First lift the deeper node, I, by one level to D, so both are at depth two.

## 8. Worked example (1:01) — `slides/08.png`

Now move both up together. E goes to B, D goes to B. They meet: the answer is B.

## 9. Java solution (1:09) — `slides/09.png`

We compute both depths by walking up to the top. Then we lift the deeper node until depths match, and finally move both up together until they're the same node.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of d. Space is constant.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

If one node is the ancestor of the other, the algorithm returns it naturally. The same node twice returns itself.

## 12. Interview tips & follow-ups (1:31) — `slides/12.png`

Without parent pointers, use the recursive lowest common ancestor. For many queries, binary lifting answers each in log time.

## 13. Recap (1:40) — `slides/13.png`

To recap Youngest Common Ancestor: Bring both descendants to the same depth, then climb together until they meet. Try re-implementing it from scratch without looking.
