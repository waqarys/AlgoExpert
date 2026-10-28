package veryhard.binarytrees;

import common.BinaryTree;

/**
 * All Kinds Of Node Depths: sum, over every node, of the depths of all nodes in its subtree (relative to it).
 * Per subtree: sumDepths = sumDepths(l) + size(l) + sumDepths(r) + size(r).
 * Time: O(n) | Space: O(h).
 */
public class AllKindsOfNodeDepths {
    public static int allKindsOfNodeDepths(BinaryTree root) { return (int) info(root)[2]; }

    /** returns {size, sumDepths, total} */
    private static long[] info(BinaryTree t) {
        if (t == null) return new long[]{0, 0, 0};
        long[] l = info(t.left), r = info(t.right);
        long size = 1 + l[0] + r[0], depths = l[1] + l[0] + r[1] + r[0];
        return new long[]{size, depths, depths + l[2] + r[2]};
    }
}
