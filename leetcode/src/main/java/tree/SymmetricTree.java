package tree;

import common.tree.TreeNode;

public class SymmetricTree {

    public boolean isSymmetric(TreeNode root) {
        if(root == null) {
            return true;
        }

        return checkSymmetricChildren(root.getLeft(), root.getRight());
    }

    private boolean checkSymmetricChildren(TreeNode left, TreeNode right) {
        if(left == null && right == null) return true;
        if(left == null && right != null) return false;
        if(left != null && right == null) return false;
        if(left.val == right.val){
            return checkSymmetricChildren(left.left, right.right) && checkSymmetricChildren(left.right, right.left);
        } else {
            return false;
        }
    }
}
