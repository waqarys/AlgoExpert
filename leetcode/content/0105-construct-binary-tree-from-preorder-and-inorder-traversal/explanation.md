# 0105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Problem
- Given preorder and inorder traversals of a tree with unique values, rebuild the tree.

## Intuition
- preorder[0] is the root. Its position in inorder splits the remaining values into the left subtree (before it) and the right subtree (after it).
- The left subtree size tells us how many of the following preorder values belong to the left.

## Brute Force
- Search the root in inorder linearly and slice arrays each time: O(n^2) time and memory.

## Optimal Approach
1. Map value -> inorder index.
2. build(inLo, inHi) uses a global preorder pointer: root = pre[p++]; mid = index[root].
3. root.left = build(inLo, mid-1); root.right = build(mid+1, inHi). Left must be built first because preorder lists left before right.

## Worked Example
- pre = [3,9,20,15,7], in = [9,3,15,20,7].
```text
root 3 (in idx 1): left in[0..0]  right in[2..4]
  left: root 9 leaf
  right: root 20 (in idx 3): left 15, right 7
tree [3,9,20,null,null,15,7]
```

## Complexity
- Time: O(n). Space: O(n) for the map plus O(h) recursion.

## Pitfalls
- Building right before left consumes preorder in the wrong order.

## Video Script
- Colour-code the root, left block and right block in both arrays.

## Solution
```java file=trees/ConstructBinaryTreeFromPreorderInorder.java
package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 105 Construct Binary Tree from Preorder and Inorder Traversal.
 * Approach: preorder pointer picks roots; inorder index map splits left/right ranges.
 * Time O(n), Space O(n).
 */
public class ConstructBinaryTreeFromPreorderInorder {
    private int p;
    private int[] pre;
    private Map<Integer, Integer> idx;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        pre = preorder;
        p = 0;
        idx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) idx.put(inorder[i], i);
        return build(0, inorder.length - 1);
    }

    private TreeNode build(int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(pre[p++]);
        int mid = idx.get(root.val);
        root.left = build(lo, mid - 1);
        root.right = build(mid + 1, hi);
        return root;
    }
}
```

## Tests
```java test=trees/ConstructBinaryTreeFromPreorderInorderTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class ConstructBinaryTreeFromPreorderInorderTest {
    ConstructBinaryTreeFromPreorderInorder s = new ConstructBinaryTreeFromPreorderInorder();
    @Test void examples() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7),
                TreeNode.toList(s.buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7})));
        assertEquals(List.of(-1), TreeNode.toList(s.buildTree(new int[]{-1}, new int[]{-1})));
        assertEquals(Arrays.asList(1, null, 2, null, 3),
                TreeNode.toList(s.buildTree(new int[]{1, 2, 3}, new int[]{1, 2, 3})));
    }
}
```
