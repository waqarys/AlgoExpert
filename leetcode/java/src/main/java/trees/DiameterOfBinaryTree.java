package trees;

import common.TreeNode;

/**
 * LC 543 Diameter of Binary Tree.
 * Approach: DFS returns height; at each node update best with leftHeight + rightHeight.
 * Time O(n), Space O(h).
 */
public class DiameterOfBinaryTree {
    private int best;

    public int diameterOfBinaryTree(TreeNode root) {
        best = 0;
        height(root);
        return best;
    }

    private int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left), r = height(n.right);
        best = Math.max(best, l + r);
        return 1 + Math.max(l, r);
    }
}
