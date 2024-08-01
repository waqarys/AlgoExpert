package tree;

import common.tree.TreeNode;

public class MergeBinaryTrees {

    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if(t1 == null && t2 == null) return null;
        if(t1 == null) return t2;
        if(t2 == null) return t1;

        TreeNode output = new TreeNode(t1.val + t2.val);
        output.left = mergeTrees(t1.left, t2.left);
        output.right = mergeTrees(t1.right, t2.right);
        return output;
    }
}
