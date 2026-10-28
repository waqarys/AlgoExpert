public class SplitBinaryTree {
    public static int splitBinaryTree(BinaryTree t) {
        int total = sum(t);
        if (total % 2 != 0) return 0;
        boolean[] found = {false};
        check(t, total / 2, found, true);
        return found[0] ? total / 2 : 0;
    }

    private static int sum(BinaryTree t) { return t == null ? 0 : t.value + sum(t.left) + sum(t.right); }

    private static int check(BinaryTree t, int half, boolean[] found, boolean root) {
        if (t == null) return 0;
        int s = t.value + check(t.left, half, found, false) + check(t.right, half, found, false);
        if (!root && s == half) found[0] = true;
        return s;
    }
}
