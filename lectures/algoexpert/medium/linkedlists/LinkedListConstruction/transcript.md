# AlgoExpert · Linked List Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Linked List Construction (0:00) — `slides/01.png`

Let's solve Linked List Construction, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Doubly linked list with head or tail supporting setHead, setTail, insertBefore, insertAfter, insertAtPosition (1-based), removeNodesWithValue, remove and containsNodeWithValue. Inserting a node already in the list moves it.

## 3. Intuition (0:28) — `slides/03.png`

A doubly linked list keeps head and tail pointers so most operations rewire a few links.

## 4. Brute force vs optimal (0:34) — `slides/04.png`

With a singly linked list, removing a node needs its predecessor, which means a scan. Doubly linked nodes know both neighbours, so inserting and removing a known node is constant time.

## 5. Approach (0:45) — `slides/05.png`

Step by step. First, remove a node from its spot before reinserting. Second, update head and tail on the edges. Third, walk for position and value ops.

## 6. Worked example (0:57) — `slides/06.png`

Set head to one: the list was empty, so one is both head and tail.

## 7. Worked example (1:02) — `slides/07.png`

Set tail to four: insert after the current tail.

## 8. Worked example (1:06) — `slides/08.png`

Insert three before four: rewire three's prev to one and next to four, then fix both neighbours.

## 9. Worked example (1:13) — `slides/09.png`

Insert two at position two, walking from the head to the node currently there.

## 10. Worked example (1:18) — `slides/10.png`

Remove nodes with value three: unlink by connecting its prev and next, and clear its pointers.

## 11. Java solution (1/4) (1:25) — `slides/11.png`

Set head and set tail handle the empty case and otherwise delegate to insert before or after. Insert before removes the node, wires its prev and next, and updates either head or the previous node's next.

## 12. Java solution (2/4) (1:37) — `slides/12.png`

Set head and set tail handle the empty case and otherwise delegate to insert before or after. Insert before removes the node, wires its prev and next, and updates either head or the previous node's next.

## 13. Java solution (3/4) (1:50) — `slides/13.png`

Set head and set tail handle the empty case and otherwise delegate to insert before or after. Insert before removes the node, wires its prev and next, and updates either head or the previous node's next.

## 14. Java solution (4/4) (2:03) — `slides/14.png`

Set head and set tail handle the empty case and otherwise delegate to insert before or after. Insert before removes the node, wires its prev and next, and updates either head or the previous node's next.

## 15. Complexity (2:16) — `slides/15.png`

Time is constant for head or tail or insertBefore or After or remove, O of n for position or value ops. Space is constant.

## 16. Edge cases & pitfalls (2:25) — `slides/16.png`

If the node being inserted is already in the list, remove it first. Always update head and tail when operating at the ends.

## 17. Interview tips & follow-ups (2:34) — `slides/17.png`

Draw the pointer changes before coding. This structure is the backbone of an LRU cache.

## 18. Recap (2:41) — `slides/18.png`

To recap Linked List Construction: A doubly linked list keeps head and tail pointers so most operations rewire a few links. Try re-implementing it from scratch without looking.
