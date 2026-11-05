# 0199. Binary Tree Right Side View

**Difficulty:** Medium | **Category:** Trees | **LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

## Problem
- Return the values visible when looking at the tree from the right: the last node of each level, top to bottom.

## Intuition
- Level-order BFS; the last node popped in each level is visible.
- DFS alternative: visit right child first and record the first node seen at each new depth.

## Brute Force
- Full level-order traversal then take the last of each list: same complexity, more memory.

## Optimal Approach
1. BFS by level.
2. For each level, record the value of the node at index size-1.

## Worked Example
- [1,2,3,null,5,null,4].
```text
level [1]    -> 1
level [2,3]  -> 3
level [5,4]  -> 4
answer [1,3,4]
```

## Complexity
- Time: O(n). Space: O(width).

## Pitfalls
- A left node can be visible if the right side is shorter ([1,2] -> [1,2]).

## Video Script
- Contrast "rightmost child" (wrong) with "rightmost per level" (right) using [1,2,3,4].

## Solution
```java file=trees/BinaryTreeRightSideView.java
package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 199 Binary Tree Right Side View.
 * Approach: BFS by level, record the last node of each level.
 * Time O(n), Space O(n).
 */
public class BinaryTreeRightSideView {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>(List.of(root));
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                if (i == size - 1) res.add(n.val);
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
        }
        return res;
    }
}
```

## Tests
```java test=trees/BinaryTreeRightSideViewTest.java
package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class BinaryTreeRightSideViewTest {
    BinaryTreeRightSideView s = new BinaryTreeRightSideView();
    @Test void examples() {
        assertEquals(List.of(1, 3, 4), s.rightSideView(TreeNode.of(1, 2, 3, null, 5, null, 4)));
        assertEquals(List.of(1, 3), s.rightSideView(TreeNode.of(1, null, 3)));
        assertEquals(List.of(1, 3, 4), s.rightSideView(TreeNode.of(1, 2, 3, 4)));
        assertEquals(List.of(), s.rightSideView(null));
    }
}
```
