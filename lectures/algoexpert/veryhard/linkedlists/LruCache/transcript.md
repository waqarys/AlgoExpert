# AlgoExpert · Lru Cache

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Lru Cache (0:00) — `slides/01.png`

Let's solve Lru Cache, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. InsertKeyValuePair, getValueFromKey (null if missing) and getMostRecentKey, evicting the least recently used key at capacity. Hash map plus doubly linked list.

## 3. Intuition (0:24) — `slides/03.png`

A hash map for lookup plus a doubly linked list for recency order gives constant-time operations.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, map keys to nodes. Second, move accessed nodes to the head. Third, evict the tail at capacity. Fourth, most recent key is the head.

## 5. Java solution (1/2) (0:45) — `slides/05.png`

Here's the Java solution, starting with lru cache. It follows the steps we just described.

## 6. Java solution (2/2) (0:52) — `slides/06.png`

Continuing with get value from key, get most recent key, move to front.

## 7. Complexity (0:57) — `slides/07.png`

Time is constant per op. Space is O of capacity.

## 8. Recap (1:01) — `slides/08.png`

To recap Lru Cache: A hash map for lookup plus a doubly linked list for recency order gives constant-time operations. Try re-implementing it from scratch without looking.
