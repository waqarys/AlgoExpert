package common;

/** Shared binary tree node (value, children, optional parent) used by tree problems. */
public class BinaryTree {
    public int value;
    public BinaryTree left;
    public BinaryTree right;
    public BinaryTree parent;

    public BinaryTree(int value) { this.value = value; }

    public BinaryTree(int value, BinaryTree left, BinaryTree right) {
        this.value = value;
        this.left = left;
        this.right = right;
        if (left != null) left.parent = this;
        if (right != null) right.parent = this;
    }

    /** Builds a tree from a level-order array; null entries mean missing nodes. */
    public static BinaryTree fromLevelOrder(Integer... values) {
        if (values.length == 0 || values[0] == null) return null;
        BinaryTree[] nodes = new BinaryTree[values.length];
        for (int i = 0; i < values.length; i++) if (values[i] != null) nodes[i] = new BinaryTree(values[i]);
        java.util.ArrayDeque<BinaryTree> queue = new java.util.ArrayDeque<>();
        queue.add(nodes[0]);
        int i = 1;
        while (!queue.isEmpty() && i < values.length) {
            BinaryTree cur = queue.poll();
            if (i < values.length) { cur.left = nodes[i]; if (nodes[i] != null) { nodes[i].parent = cur; queue.add(nodes[i]); } i++; }
            if (i < values.length) { cur.right = nodes[i]; if (nodes[i] != null) { nodes[i].parent = cur; queue.add(nodes[i]); } i++; }
        }
        return nodes[0];
    }

    public static java.util.List<Integer> inOrder(BinaryTree t) {
        java.util.List<Integer> out = new java.util.ArrayList<>();
        inOrder(t, out);
        return out;
    }

    private static void inOrder(BinaryTree t, java.util.List<Integer> out) {
        if (t == null) return;
        inOrder(t.left, out); out.add(t.value); inOrder(t.right, out);
    }
}
