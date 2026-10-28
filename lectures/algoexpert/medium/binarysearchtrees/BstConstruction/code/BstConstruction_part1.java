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
