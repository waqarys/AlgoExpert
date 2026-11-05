# 0100. Same Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/same-tree/

## Problem
- Return true if two binary trees have identical structure and values.

## Intuition
- Two trees are equal if their roots match and their left subtrees are equal and their right subtrees are equal.

## Brute Force
- Serialize both (with null markers) and compare strings: O(n) but extra memory.

## Optimal Approach
1. Both null -> true. One null -> false.
2. Values differ -> false.
3. Return same(p.left, q.left) && same(p.right, q.right).

## Worked Example
- p = [1,2], q = [1,null,2].
```text
roots 1 == 1
left: p.left=2, q.left=null -> false
```

## Complexity
- Time: O(min(n, m)). Space: O(h).

## Pitfalls
- Handle the null cases before reading .val.

## Video Script
- Base cases are the whole problem; draw the 2x2 grid of null/non-null.

## Solution
```java file=trees/SameTree.java
package trees;

import common.TreeNode;

/**
 * LC 100 Same Tree.
 * Approach: simultaneous DFS comparing structure and values.
 * Time O(n), Space O(h).
 */
public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null || q == null) return p == q;
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

## Tests
```java test=trees/SameTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SameTreeTest {
    SameTree s = new SameTree();
    @Test void examples() {
        assertTrue(s.isSameTree(TreeNode.of(1, 2, 3), TreeNode.of(1, 2, 3)));
        assertFalse(s.isSameTree(TreeNode.of(1, 2), TreeNode.of(1, null, 2)));
        assertFalse(s.isSameTree(TreeNode.of(1, 2, 1), TreeNode.of(1, 1, 2)));
        assertTrue(s.isSameTree(null, null));
    }
}
```
