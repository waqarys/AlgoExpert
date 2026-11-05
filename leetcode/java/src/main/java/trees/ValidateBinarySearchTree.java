package trees;

import common.TreeNode;

/**
 * LC 98 Validate Binary Search Tree.
 * Approach: DFS with (low, high) exclusive bounds inherited from ancestors; long bounds avoid overflow.
 * Time O(n), Space O(h).
 */
public class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) { return valid(root, Long.MIN_VALUE, Long.MAX_VALUE); }

    private boolean valid(TreeNode n, long low, long high) {
        if (n == null) return true;
        if (n.val <= low || n.val >= high) return false;
        return valid(n.left, low, n.val) && valid(n.right, n.val, high);
    }
}
