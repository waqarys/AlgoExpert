# 0226. Invert Binary Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/invert-binary-tree/

## Problem
- Mirror a binary tree: swap the left and right child of every node, and return the root.

## Intuition
- An inverted tree is a root whose children are the inverted right and inverted left subtrees: a perfect recursive definition.

## Brute Force
- There is no slower "brute force"; the only choice is recursive DFS versus iterative BFS with a queue.

## Optimal Approach
1. If root is null, return null.
2. Swap root.left and root.right.
3. Recurse on both children.

## Worked Example
- [4,2,7,1,3,6,9].
```text
      4              4
    /   \          /   \
   2     7   ->   7     2
  / \   / \      / \   / \
 1   3 6   9    9   6 3   1
```

## Complexity
- Time: O(n). Space: O(h) recursion (h = height).

## Pitfalls
- Swap with a temp variable, or assign from saved recursive results; never overwrite before reading.

## Video Script
- Famous "Homebrew" interview anecdote as a hook, then a 4-line solution.

## Solution
```java file=trees/InvertBinaryTree.java
package trees;

import common.TreeNode;

/**
 * LC 226 Invert Binary Tree.
 * Approach: recursive DFS swapping children at every node.
 * Time O(n), Space O(h).
 */
public class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode tmp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(tmp);
        return root;
    }
}
```

## Tests
```java test=trees/InvertBinaryTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class InvertBinaryTreeTest {
    InvertBinaryTree s = new InvertBinaryTree();
    @Test void examples() {
        assertEquals(Arrays.asList(4, 7, 2, 9, 6, 3, 1), TreeNode.toList(s.invertTree(TreeNode.of(4, 2, 7, 1, 3, 6, 9))));
        assertEquals(Arrays.asList(2, 3, 1), TreeNode.toList(s.invertTree(TreeNode.of(2, 1, 3))));
        assertNull(s.invertTree(null));
    }
}
```
