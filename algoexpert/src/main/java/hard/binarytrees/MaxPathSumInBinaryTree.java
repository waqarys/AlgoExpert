package hard.binarytrees;

import common.BinaryTree;

/**
 * Max Path Sum In Binary Tree: maximum sum over any path (node-to-node, no repeats).
 * Time: O(n) | Space: O(h).
 */
public class MaxPathSumInBinaryTree {
    public static int maxPathSum(BinaryTree t) { int[] best = {Integer.MIN_VALUE}; branch(t, best); return best[0]; }

    private static int branch(BinaryTree t, int[] best) {
        if (t == null) return 0;
        int l = Math.max(0, branch(t.left, best)), r = Math.max(0, branch(t.right, best));
        best[0] = Math.max(best[0], t.value + l + r);
        return t.value + Math.max(l, r);
    }
}
