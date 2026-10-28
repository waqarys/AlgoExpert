# AlgoExpert · Lru Cache

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Lru Cache (0:00) — `slides/01.png`

Let's solve Lru Cache, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. InsertKeyValuePair, getValueFromKey (null if missing) and getMostRecentKey, evicting the least recently used key at capacity. Hash map plus doubly linked list.

## 3. Intuition (0:24) — `slides/03.png`

A hash map for lookup plus a doubly linked list for recency order gives constant-time operations.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

A list needs a scan to find and move keys. A hash map pointing into a doubly linked list gives constant-time lookup, move-to-front and eviction.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, map keys to nodes. Second, move accessed nodes to the head. Third, evict the tail at capacity. Fourth, most recent key is the head.

## 6. Worked example (0:54) — `slides/06.png`

Insert b and move it to the front.

## 7. Worked example (0:58) — `slides/07.png`

Insert a and move it to the front.

## 8. Worked example (1:01) — `slides/08.png`

Insert c and move it to the front.

## 9. Worked example (1:04) — `slides/09.png`

Read a and move it to the front.

## 10. Worked example (1:08) — `slides/10.png`

Insert d and move it to the front. Over capacity, so evict the least recent, b.

## 11. Java solution (1/2) (1:15) — `slides/11.png`

Insert updates and moves an existing node, otherwise evicts the tail's previous node if full and adds a new node at the front. Get moves the node to the front and returns its value.

## 12. Java solution (2/2) (1:26) — `slides/12.png`

Insert updates and moves an existing node, otherwise evicts the tail's previous node if full and adds a new node at the front. Get moves the node to the front and returns its value.

## 13. Complexity (1:37) — `slides/13.png`

Time is constant per op. Space is O of capacity.

## 14. Edge cases & pitfalls (1:41) — `slides/14.png`

Updating an existing key also refreshes it.

## 15. Interview tips & follow-ups (1:45) — `slides/15.png`

Java's linked hash map can do this with access order.

## 16. Recap (1:50) — `slides/16.png`

To recap Lru Cache: A hash map for lookup plus a doubly linked list for recency order gives constant-time operations. Try re-implementing it from scratch without looking.
