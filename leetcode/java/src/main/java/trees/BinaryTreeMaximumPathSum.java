package trees;

import common.TreeNode;

/**
 * LC 124 Binary Tree Maximum Path Sum.
 * Approach: DFS returns best downward arm; at each node update best with val + left arm + right arm.
 * Time O(n), Space O(h).
 */
public class BinaryTreeMaximumPathSum {
    private int best;

    public int maxPathSum(TreeNode root) {
        best = Integer.MIN_VALUE;
        gain(root);
        return best;
    }

    private int gain(TreeNode n) {
        if (n == null) return 0;
        int l = Math.max(0, gain(n.left)), r = Math.max(0, gain(n.right));
        best = Math.max(best, n.val + l + r);
        return n.val + Math.max(l, r);
    }
}
