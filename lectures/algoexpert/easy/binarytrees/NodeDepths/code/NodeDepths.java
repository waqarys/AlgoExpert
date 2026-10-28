public class NodeDepths {
    public static int nodeDepths(BinaryTree root) { return sum(root, 0); }

    private static int sum(BinaryTree n, int depth) {
        if (n == null) return 0;
        return depth + sum(n.left, depth + 1) + sum(n.right, depth + 1);
    }
}
