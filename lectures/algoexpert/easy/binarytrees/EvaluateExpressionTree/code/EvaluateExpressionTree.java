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
