public class MergeBinaryTrees {
    public static BinaryTree mergeBinaryTrees(BinaryTree a, BinaryTree b) {
        if (a == null) return b;
        if (b == null) return a;
        a.value += b.value;
        a.left = mergeBinaryTrees(a.left, b.left);
        a.right = mergeBinaryTrees(a.right, b.right);
        return a;
    }
}
