package common;

/** Shared binary search tree node. Insert keeps duplicates in the right subtree. */
public class BST {
    public int value;
    public BST left;
    public BST right;

    public BST(int value) { this.value = value; }

    public BST insert(int v) {
        BST cur = this;
        while (true) {
            if (v < cur.value) { if (cur.left == null) { cur.left = new BST(v); break; } cur = cur.left; }
            else { if (cur.right == null) { cur.right = new BST(v); break; } cur = cur.right; }
        }
        return this;
    }

    public static BST of(int... values) {
        BST root = new BST(values[0]);
        for (int i = 1; i < values.length; i++) root.insert(values[i]);
        return root;
    }

    public static java.util.List<Integer> inOrder(BST t) {
        java.util.List<Integer> out = new java.util.ArrayList<>();
        walk(t, out);
        return out;
    }

    private static void walk(BST t, java.util.List<Integer> out) {
        if (t == null) return;
        walk(t.left, out); out.add(t.value); walk(t.right, out);
    }
}
