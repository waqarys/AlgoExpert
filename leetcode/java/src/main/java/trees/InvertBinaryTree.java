package trees;

import common.TreeNode;

/**
 * LC 226 Invert Binary Tree.
 * Approach: recursive DFS swapping children at every node.
 * Time O(n), Space O(h).
 */
public class InvertBinaryTree {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode tmp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(tmp);
        return root;
    }
}
