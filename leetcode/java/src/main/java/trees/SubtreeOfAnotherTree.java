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
