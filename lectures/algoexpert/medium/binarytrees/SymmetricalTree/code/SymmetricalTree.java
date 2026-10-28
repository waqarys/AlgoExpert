public class SymmetricalTree {
    public static boolean symmetricalTree(BinaryTree t) { return t == null || mirror(t.left, t.right); }

    private static boolean mirror(BinaryTree a, BinaryTree b) {
        if (a == null || b == null) return a == b;
        return a.value == b.value && mirror(a.left, b.right) && mirror(a.right, b.left);
    }
}
