public class IterativeInOrderTraversal {
    public static void iterativeInOrderTraversal(BinaryTree tree, Consumer<BinaryTree> callback) {
        BinaryTree prev = null, cur = tree;
        while (cur != null) {
            BinaryTree next;
            if (prev == null || prev == cur.parent) {
                if (cur.left != null) next = cur.left;
                else { callback.accept(cur); next = cur.right != null ? cur.right : cur.parent; }
            } else if (prev == cur.left) {
                callback.accept(cur);
                next = cur.right != null ? cur.right : cur.parent;
            } else next = cur.parent;
            prev = cur;
            cur = next;
        }
    }
}
