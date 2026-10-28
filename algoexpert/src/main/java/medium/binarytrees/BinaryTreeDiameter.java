package medium.binarytrees;

import common.BinaryTree;

/**
 * Binary Tree Diameter: number of edges on the longest path between any two nodes.
 * Time: O(n) | Space: O(h).
 */
public class BinaryTreeDiameter {
    public static int binaryTreeDiameter(BinaryTree t) {
        int[] best = {0};
        height(t, best);
        return best[0];
    }

    private static int height(BinaryTree t, int[] best) {
        if (t == null) return 0;
        int l = height(t.left, best), r = height(t.right, best);
        best[0] = Math.max(best[0], l + r);
        return 1 + Math.max(l, r);
    }
}
