# 0230. Kth Smallest Element in a BST

**Difficulty:** Medium | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Problem
- Return the k-th smallest value (1-indexed) in a BST.

## Intuition
- Inorder traversal of a BST visits values in sorted order, so the k-th visited node is the answer.
- An iterative stack lets us stop as soon as we reach k.

## Brute Force
- Collect all values, sort, index: O(n log n).

## Optimal Approach
1. cur = root, stack empty.
2. Push all left children; pop a node; k--; if k == 0 return it.
3. Move to its right child and repeat.

## Worked Example
- [5,3,6,2,4,null,null,1], k = 3.
```text
push 5,3,2,1
pop 1 (k=2) ; pop 2 (k=1) ; pop 3 (k=0) -> answer 3
```

## Complexity
- Time: O(h + k). Space: O(h).

## Pitfalls
- Follow-up (frequent inserts/deletes): augment nodes with subtree sizes for O(h) queries.

## Video Script
- "Inorder of a BST is sorted" - the single most useful BST fact.

## Solution
```java file=trees/KthSmallestElementInBST.java
package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 230 Kth Smallest Element in a BST.
 * Approach: iterative inorder traversal, stop at the k-th popped node.
 * Time O(h + k), Space O(h).
 */
public class KthSmallestElementInBST {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop();
            if (--k == 0) return cur.val;
            cur = cur.right;
        }
        throw new IllegalArgumentException("k larger than tree size");
    }
}
```

## Tests
```java test=trees/KthSmallestElementInBSTTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KthSmallestElementInBSTTest {
    KthSmallestElementInBST s = new KthSmallestElementInBST();
    @Test void examples() {
        assertEquals(1, s.kthSmallest(TreeNode.of(3, 1, 4, null, 2), 1));
        assertEquals(3, s.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 3));
        assertEquals(6, s.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 6));
    }
}
```
