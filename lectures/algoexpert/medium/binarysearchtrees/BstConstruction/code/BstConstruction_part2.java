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
