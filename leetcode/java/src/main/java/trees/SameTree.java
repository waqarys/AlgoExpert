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
