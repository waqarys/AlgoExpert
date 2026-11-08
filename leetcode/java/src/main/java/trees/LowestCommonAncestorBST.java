package trees;

import common.TreeNode;

/**
 * LC 235 Lowest Common Ancestor of a BST.
 * Approach: walk down; go left if both smaller, right if both larger, else current is the LCA.
 * Time O(h), Space O(1).
 */
public class LowestCommonAncestorBST {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode cur = root;
        while (cur != null) {
            if (p.val < cur.val && q.val < cur.val) cur = cur.left;
            else if (p.val > cur.val && q.val > cur.val) cur = cur.right;
            else return cur;
        }
        return null;
    }
}
