package easy.binarytrees;

import common.BinaryTree;

/**
 * Evaluate Expression Tree: leaves are positive ints; internal nodes encode operators
 * -1 '+', -2 '-', -3 '/' (truncating), -4 '*'. Evaluate the tree.
 * Time: O(n) | Space: O(h).
 */
public class EvaluateExpressionTree {
    public static int evaluateExpressionTree(BinaryTree t) {
        if (t.value >= 0) return t.value;
        int l = evaluateExpressionTree(t.left), r = evaluateExpressionTree(t.right);
        return switch (t.value) {
            case -1 -> l + r;
            case -2 -> l - r;
            case -3 -> l / r;
            default -> l * r;
        };
    }
}
