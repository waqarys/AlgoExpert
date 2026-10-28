public class FindSuccessor {
    public static BinaryTree findSuccessor(BinaryTree tree, BinaryTree node) {
        if (node.right != null) {
            BinaryTree c = node.right;
            while (c.left != null) c = c.left;
            return c;
        }
        BinaryTree c = node;
        while (c.parent != null && c.parent.right == c) c = c.parent;
        return c.parent;
    }
}
