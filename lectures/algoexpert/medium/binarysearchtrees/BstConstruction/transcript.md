# AlgoExpert · Bst Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bst Construction (0:00) — `slides/01.png`

Let's solve Bst Construction, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A BST class supporting insert, contains and remove (duplicates go right; removing a node with two children replaces it with its in-order successor's value). Removing the only node is a no-op.

## 3. Intuition (0:26) — `slides/03.png`

Insert, search and remove all follow the BST ordering; removal of a two-child node swaps in the smallest value of the right subtree.

## 4. Brute force vs optimal (0:34) — `slides/04.png`

A sorted array gives fast search but slow inserts. A BST makes insert, search and remove all proportional to the height: log n on average, but linear if the tree degenerates. Self-balancing trees guarantee log n.

## 5. Approach (0:49) — `slides/05.png`

Step by step. First, walk left or right by comparison. Second, insert at the empty spot. Third, to remove with two children, copy the right subtree's minimum and delete it there. Fourth, handle the root carefully.

## 6. Worked example (1:05) — `slides/06.png`

Here's a BST built by inserting ten, five, fifteen, two, five, thirteen, twenty-two and one. Equal values go right.

## 7. Worked example (1:15) — `slides/07.png`

To insert fourteen, compare with 10: fourteen is larger, so go right.

## 8. Worked example (1:20) — `slides/08.png`

To insert fourteen, compare with 15: fourteen is smaller, so go left.

## 9. Worked example (1:26) — `slides/09.png`

To insert fourteen, compare with 13: fourteen is larger, so go right.

## 10. Worked example (1:31) — `slides/10.png`

Thirteen has no right child, so fourteen goes there.

## 11. Worked example (1:35) — `slides/11.png`

Removing the root, ten, which has two children: copy the smallest value of its right subtree, thirteen, into the root, then remove thirteen from the right subtree, where it has at most one child.

## 12. Worked example (1:46) — `slides/12.png`

The result: thirteen at the root, and fourteen takes thirteen's old place.

## 13. Java solution (1/2) (1:52) — `slides/13.png`

Insert walks down comparing values, going left for smaller and right otherwise, and attaches a new node at the first empty spot. Contains walks the same way and returns true on equality.

## 14. Java solution (2/2) (2:03) — `slides/14.png`

Remove finds the node while tracking its parent. With two children, it copies the right subtree's minimum and removes that. With one child, it splices the child in, handling the root specially by copying the child's value and pointers.

## 15. Complexity (2:18) — `slides/15.png`

Time is O of log n avg, O of n worst per op. Space is constant (iterative).

## 16. Edge cases & pitfalls (2:24) — `slides/16.png`

The nastiest case is removing the root when it has only one child, since there's no parent to relink. Be consistent that equal values go right.

## 17. Interview tips & follow-ups (2:33) — `slides/17.png`

Iterative versions avoid recursion overhead. Follow-ups include balancing and augmenting nodes with subtree sizes.

## 18. Recap (2:42) — `slides/18.png`

To recap Bst Construction: Insert, search and remove all follow the BST ordering; removal of a two-child node swaps in the smallest value of the right subtree. Try re-implementing it from scratch without looking.
