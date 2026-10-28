package medium.binarytrees;

import common.BinaryTree;

/**
 * Height Balanced Binary Tree: for every node, do left/right subtree heights differ by at most 1?
 * Returns -1 from the helper as an "unbalanced" sentinel.
 * Time: O(n) | Space: O(h).
 */
public class HeightBalancedBinaryTree {
    public static boolean heightBalancedBinaryTree(BinaryTree t) { return h(t) != -1; }

    private static int h(BinaryTree t) {
        if (t == null) return 0;
        int l = h(t.left), r = h(t.right);
        if (l == -1 || r == -1 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
