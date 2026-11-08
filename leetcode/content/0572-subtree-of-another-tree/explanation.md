# 0572. Subtree of Another Tree

**Difficulty:** Easy | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/subtree-of-another-tree/

## Problem
- Return true if subRoot appears in root as a node together with all its descendants.

## Intuition
- Try every node of root as a candidate and check Same Tree (problem 100).

## Brute Force
- That direct approach is O(m * n) and is the expected answer.
- Faster: serialize both with null markers and use string matching (KMP) for O(m + n).

## Optimal Approach
1. If root is null return false.
2. If sameTree(root, subRoot) return true.
3. Return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot).

## Worked Example
- root = [3,4,5,1,2], subRoot = [4,1,2].
```text
at 3: same(3..., 4...) false
at 4: same([4,1,2],[4,1,2]) true -> answer true
```

## Complexity
- Time: O(m * n) worst case. Space: O(h).

## Pitfalls
- A matching subtree must match all the way to the leaves: [3,4,5,1,2,null,null,null,null,0] vs [4,1,2] is false.

## Video Script
- Reuse problem 100 as a helper, then mention the serialization + KMP upgrade.

## Solution
```java file=trees/SubtreeOfAnotherTree.java
package trees;

import common.TreeNode;

/**
 * LC 572 Subtree of Another Tree.
 * Approach: at every node of root, test sameTree with subRoot.
 * Time O(m*n), Space O(h).
 */
public class SubtreeOfAnotherTree {
    public boolean isSubtree(TreeNode root, TreeNode sub) {
        if (root == null) return sub == null;
        if (same(root, sub)) return true;
        return isSubtree(root.left, sub) || isSubtree(root.right, sub);
    }

    private boolean same(TreeNode a, TreeNode b) {
        if (a == null || b == null) return a == b;
        return a.val == b.val && same(a.left, b.left) && same(a.right, b.right);
    }
}
```

## Tests
```java test=trees/SubtreeOfAnotherTreeTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SubtreeOfAnotherTreeTest {
    SubtreeOfAnotherTree s = new SubtreeOfAnotherTree();
    @Test void examples() {
        assertTrue(s.isSubtree(TreeNode.of(3, 4, 5, 1, 2), TreeNode.of(4, 1, 2)));
        assertFalse(s.isSubtree(TreeNode.of(3, 4, 5, 1, 2, null, null, null, null, 0), TreeNode.of(4, 1, 2)));
        assertTrue(s.isSubtree(TreeNode.of(1, 1), TreeNode.of(1)));
    }
}
```
