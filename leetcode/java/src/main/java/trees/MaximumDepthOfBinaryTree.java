package trees;

import common.TreeNode;

/**
 * LC 104 Maximum Depth of Binary Tree.
 * Approach: post-order DFS, 1 + max(child depths).
 * Time O(n), Space O(h).
 */
public class MaximumDepthOfBinaryTree {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
