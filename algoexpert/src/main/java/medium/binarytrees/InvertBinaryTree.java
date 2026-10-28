package medium.binarytrees;

import common.BinaryTree;

/**
 * Invert Binary Tree: mirror the tree by swapping every node's children.
 * Time: O(n) | Space: O(h).
 */
public class InvertBinaryTree {
    public static void invertBinaryTree(BinaryTree t) {
        if (t == null) return;
        BinaryTree tmp = t.left; t.left = t.right; t.right = tmp;
        invertBinaryTree(t.left);
        invertBinaryTree(t.right);
    }
}
