# AlgoExpert · Linked List Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Linked List Construction (0:00) — `slides/01.png`

Let's solve Linked List Construction, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Doubly linked list with head or tail supporting setHead, setTail, insertBefore, insertAfter, insertAtPosition (1-based), removeNodesWithValue, remove and containsNodeWithValue. Inserting a node already in the list moves it.

## 3. Intuition (0:28) — `slides/03.png`

A doubly linked list keeps head and tail pointers so most operations rewire a few links.

## 4. Approach (0:34) — `slides/04.png`

Step by step. First, remove a node from its spot before reinserting. Second, update head and tail on the edges. Third, walk for position and value ops.

## 5. Java solution (1/4) (0:46) — `slides/05.png`

Here's the Java solution, starting with node. It follows the steps we just described.

## 6. Java solution (2/4) (0:53) — `slides/06.png`

Continuing with set head, set tail, insert before.

## 7. Java solution (3/4) (0:57) — `slides/07.png`

Continuing with insert after, insert at position, remove nodes with value.

## 8. Java solution (4/4) (1:03) — `slides/08.png`

Continuing with remove, contains node with value.

## 9. Complexity (1:07) — `slides/09.png`

Time is constant for head or tail or insertBefore or After or remove, O of n for position or value ops. Space is constant.

## 10. Recap (1:16) — `slides/10.png`

To recap Linked List Construction: A doubly linked list keeps head and tail pointers so most operations rewire a few links. Try re-implementing it from scratch without looking.
