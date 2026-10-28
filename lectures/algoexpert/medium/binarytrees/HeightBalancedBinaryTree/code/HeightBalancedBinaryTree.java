public class HeightBalancedBinaryTree {
    public static boolean heightBalancedBinaryTree(BinaryTree t) { return h(t) != -1; }

    private static int h(BinaryTree t) {
        if (t == null) return 0;
        int l = h(t.left), r = h(t.right);
        if (l == -1 || r == -1 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
