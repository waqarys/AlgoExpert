# 0110. Balanced Binary Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/balanced-binary-tree/

## Problem
- A tree is height-balanced if, at every node, the left and right subtree heights differ by at most 1. Check it.

## Intuition
- Compute heights bottom-up; if any subtree is unbalanced, propagate a sentinel (-1) so we stop early.

## Brute Force
- At every node call a separate height(): O(n^2) for skewed trees.

## Optimal Approach
1. check(null) = 0.
2. l = check(left), r = check(right). If either is -1 or |l - r| > 1, return -1.
3. Else return 1 + max(l, r). Balanced iff check(root) != -1.

## Worked Example
- [1,2,2,3,3,null,null,4,4].
```text
node 3s: height 2 (children 4,4)
left 2: l=2 r=2 -> height 3 ; right 2: height 1
root: |3 - 1| = 2 > 1 -> -1 -> not balanced
```

## Complexity
- Time: O(n). Space: O(h).

## Pitfalls
- Checking only the root's balance is not enough; every node must satisfy it.

## Video Script
- Show the O(n^2) version first, then fuse height and check into one DFS.

## Solution
```java file=trees/BalancedBinaryTree.java
package trees;

import common.TreeNode;

/**
 * LC 110 Balanced Binary Tree.
 * Approach: DFS returning height, or -1 as soon as any subtree is unbalanced.
 * Time O(n), Space O(h).
 */
public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) { return check(root) != -1; }

    private int check(TreeNode n) {
        if (n == null) return 0;
        int l = check(n.left);
        if (l == -1) return -1;
        int r = check(n.right);
        if (r == -1 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
```

## Tests
```java test=trees/BalancedBinaryTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BalancedBinaryTreeTest {
    BalancedBinaryTree s = new BalancedBinaryTree();
    @Test void examples() {
        assertTrue(s.isBalanced(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertFalse(s.isBalanced(TreeNode.of(1, 2, 2, 3, 3, null, null, 4, 4)));
        assertTrue(s.isBalanced(null));
        assertFalse(s.isBalanced(TreeNode.of(1, null, 2, null, 3)));
    }
}
```
