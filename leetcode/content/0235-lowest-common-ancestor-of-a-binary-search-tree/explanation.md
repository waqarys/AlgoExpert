# 0235. Lowest Common Ancestor of a BST

**Difficulty:** Medium | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Problem
- In a BST, return the lowest node that has both p and q as descendants (a node is a descendant of itself).

## Intuition
- BST ordering tells us where p and q live. If both are smaller than the current node, the LCA is in the left subtree; if both are larger, the right.
- Otherwise they split here (or one equals the node), so this node is the LCA.

## Brute Force
- Generic binary-tree LCA (ignoring BST order): O(n).

## Optimal Approach
1. cur = root.
2. If p and q < cur, go left; if both > cur, go right; else return cur.

## Worked Example
- BST [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4.
```text
cur=6: 2<6 and 4<6 -> left
cur=2: 2 is not < 2 -> split point -> LCA = 2
```

## Complexity
- Time: O(h). Space: O(1) iterative.

## Pitfalls
- The "equal" case must return the current node.

## Video Script
- Show the BST as a sorted number line; the LCA is where p and q's paths diverge.

## Solution
```java file=trees/LowestCommonAncestorBST.java
package trees;

import common.TreeNode;

/**
 * LC 235 Lowest Common Ancestor of a BST.
 * Approach: walk down; go left if both smaller, right if both larger, else current is the LCA.
 * Time O(h), Space O(1).
 */
public class LowestCommonAncestorBST {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode cur = root;
        while (cur != null) {
            if (p.val < cur.val && q.val < cur.val) cur = cur.left;
            else if (p.val > cur.val && q.val > cur.val) cur = cur.right;
            else return cur;
        }
        return null;
    }
}
```

## Tests
```java test=trees/LowestCommonAncestorBSTTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LowestCommonAncestorBSTTest {
    @Test void examples() {
        TreeNode r = TreeNode.of(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);
        var s = new LowestCommonAncestorBST();
        assertEquals(6, s.lowestCommonAncestor(r, r.find(2), r.find(8)).val);
        assertEquals(2, s.lowestCommonAncestor(r, r.find(2), r.find(4)).val);
        assertEquals(4, s.lowestCommonAncestor(r, r.find(3), r.find(5)).val);
    }
}
```
