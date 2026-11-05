package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 105 Construct Binary Tree from Preorder and Inorder Traversal.
 * Approach: preorder pointer picks roots; inorder index map splits left/right ranges.
 * Time O(n), Space O(n).
 */
public class ConstructBinaryTreeFromPreorderInorder {
    private int p;
    private int[] pre;
    private Map<Integer, Integer> idx;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        pre = preorder;
        p = 0;
        idx = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) idx.put(inorder[i], i);
        return build(0, inorder.length - 1);
    }

    private TreeNode build(int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(pre[p++]);
        int mid = idx.get(root.val);
        root.left = build(lo, mid - 1);
        root.right = build(mid + 1, hi);
        return root;
    }
}
