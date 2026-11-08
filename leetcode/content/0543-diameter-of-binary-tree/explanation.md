# 0543. Diameter of Binary Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

## Problem
- Return the length (in edges) of the longest path between any two nodes. The path need not pass through the root.

## Intuition
- The longest path "bends" at some node: it goes down the left subtree and down the right subtree.
- Path through node = height(left) + height(right). Compute heights bottom-up and track the max of that sum.

## Brute Force
- For each node compute heights separately: O(n^2).

## Optimal Approach
1. height(null) = 0.
2. At each node: l = height(left), r = height(right); best = max(best, l + r); return 1 + max(l, r).

## Worked Example
- [1,2,3,4,5].
```text
height(4)=1 height(5)=1 -> at 2: path 1+1=2, height 2
height(3)=1             -> at 1: path 2+1=3, height 3
diameter = 3 (4-2-1-3)
```

## Complexity
- Time: O(n). Space: O(h).

## Pitfalls
- Return height but record diameter: two different quantities from one DFS.

## Video Script
- Introduce the "return one thing, update a global with another" tree pattern (reused in problem 124).

## Solution
```java file=trees/DiameterOfBinaryTree.java
package trees;

import common.TreeNode;

/**
 * LC 543 Diameter of Binary Tree.
 * Approach: DFS returns height; at each node update best with leftHeight + rightHeight.
 * Time O(n), Space O(h).
 */
public class DiameterOfBinaryTree {
    private int best;

    public int diameterOfBinaryTree(TreeNode root) {
        best = 0;
        height(root);
        return best;
    }

    private int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left), r = height(n.right);
        best = Math.max(best, l + r);
        return 1 + Math.max(l, r);
    }
}
```

## Tests
```java test=trees/DiameterOfBinaryTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DiameterOfBinaryTreeTest {
    DiameterOfBinaryTree s = new DiameterOfBinaryTree();
    @Test void examples() {
        assertEquals(3, s.diameterOfBinaryTree(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(1, s.diameterOfBinaryTree(TreeNode.of(1, 2)));
        // longest path entirely inside the left subtree
        assertEquals(4, s.diameterOfBinaryTree(TreeNode.of(1, 2, null, 3, 4, 5, null, null, 6)));
    }
}
```
