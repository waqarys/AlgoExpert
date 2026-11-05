# 0104. Maximum Depth of Binary Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Problem
- Return the number of nodes along the longest root-to-leaf path.

## Intuition
- depth(node) = 1 + max(depth(left), depth(right)), with depth(null) = 0.

## Brute Force
- Enumerate all root-to-leaf paths and take the longest - same O(n), more bookkeeping.

## Optimal Approach
1. Recursive DFS as above, or
2. BFS level by level and count levels.

## Worked Example
- [3,9,20,null,null,15,7].
```text
depth(9)=1  depth(15)=1  depth(7)=1
depth(20)=1+max(1,1)=2
depth(3)=1+max(1,2)=3
```

## Complexity
- Time: O(n). Space: O(h).

## Pitfalls
- Depth counts nodes, not edges, here.

## Video Script
- Teach "trust the recursion": assume children return correct answers and combine them.

## Solution
```java file=trees/MaximumDepthOfBinaryTree.java
package trees;

import common.TreeNode;

/**
 * LC 104 Maximum Depth of Binary Tree.
 * Approach: post-order DFS, 1 + max(child depths).
 * Time O(n), Space O(h).
 */
public class MaximumDepthOfBinaryTree {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

## Tests
```java test=trees/MaximumDepthOfBinaryTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumDepthOfBinaryTreeTest {
    MaximumDepthOfBinaryTree s = new MaximumDepthOfBinaryTree();
    @Test void examples() {
        assertEquals(3, s.maxDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(2, s.maxDepth(TreeNode.of(1, null, 2)));
        assertEquals(0, s.maxDepth(null));
    }
}
```
