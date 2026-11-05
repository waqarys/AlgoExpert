package trees;

import common.TreeNode;

/**
 * LC 110 Balanced Binary Tree.
 * Approach: DFS returning height, or -1 as soon as any subtree is unbalanced.
 * Time O(n), Space O(h).
 */
public class BalancedBinaryTree {
    public boolean isBalanced(TreeNode root) { return check(root) != -1; }

    private int check(TreeNode n) {
        if (n == null) return 0;
        int l = check(n.left);
        if (l == -1) return -1;
        int r = check(n.right);
        if (r == -1 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
