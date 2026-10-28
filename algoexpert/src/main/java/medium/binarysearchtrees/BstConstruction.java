package medium.binarysearchtrees;

/**
 * BST Construction: a BST class supporting insert, contains and remove (duplicates go right; removing a
 * node with two children replaces it with its in-order successor's value). Removing the only node is a no-op.
 * Time: O(log n) avg, O(n) worst per op | Space: O(1) (iterative).
 */
public class BstConstruction {
    public static class BST {
        public int value;
        public BST left, right;

        public BST(int value) { this.value = value; }

        public BST insert(int v) {
            BST cur = this;
            while (true) {
                if (v < cur.value) { if (cur.left == null) { cur.left = new BST(v); return this; } cur = cur.left; }
                else { if (cur.right == null) { cur.right = new BST(v); return this; } cur = cur.right; }
            }
        }

        public boolean contains(int v) {
            BST cur = this;
            while (cur != null) {
                if (v == cur.value) return true;
                cur = v < cur.value ? cur.left : cur.right;
            }
            return false;
        }

        public BST remove(int v) { remove(v, null); return this; }

        private void remove(int v, BST parent) {
            BST cur = this;
            while (cur != null) {
                if (v < cur.value) { parent = cur; cur = cur.left; }
                else if (v > cur.value) { parent = cur; cur = cur.right; }
                else {
                    if (cur.left != null && cur.right != null) {
                        cur.value = cur.right.minValue();
                        cur.right.remove(cur.value, cur);
                    } else if (parent == null) {
                        BST child = cur.left != null ? cur.left : cur.right;
                        if (child != null) { cur.value = child.value; cur.left = child.left; cur.right = child.right; }
                    } else if (parent.left == cur) parent.left = cur.left != null ? cur.left : cur.right;
                    else parent.right = cur.left != null ? cur.left : cur.right;
                    return;
                }
            }
        }

        private int minValue() { BST c = this; while (c.left != null) c = c.left; return c.value; }
    }
}
