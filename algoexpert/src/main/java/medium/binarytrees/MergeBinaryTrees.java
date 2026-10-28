package medium.binarytrees;

import common.BinaryTree;

/**
 * Merge Binary Trees: overlay two trees; overlapping nodes sum their values. Mutates and returns tree1.
 * Time: O(n) of the smaller overlap | Space: O(h).
 */
public class MergeBinaryTrees {
    public static BinaryTree mergeBinaryTrees(BinaryTree a, BinaryTree b) {
        if (a == null) return b;
        if (b == null) return a;
        a.value += b.value;
        a.left = mergeBinaryTrees(a.left, b.left);
        a.right = mergeBinaryTrees(a.right, b.right);
        return a;
    }
}
