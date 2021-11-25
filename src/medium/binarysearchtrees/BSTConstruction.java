package medium.binarysearchtrees;

/**
 * <div class="html">
 * <p>
 *   Write a <span>BST</span> class for a Binary Search Tree. The class should
 *   support:
 * </p>
 * <ul>
 *   <li>Inserting values with the <span>insert</span> method.</li>
 *   <li>
 *     Removing values with the <span>remove</span> method; this method should
 *     only remove the first instance of a given value.
 *   </li>
 *   <li>Searching for values with the <span>contains</span> method.</li>
 * </ul>
 * <p>
 *   Note that you can't remove values from a single-node tree. In other words,
 *   calling the <span>remove</span> method on a single-node tree should simply not
 *   do anything.
 * </p>
 * <p>
 *   Each <span>BST</span> node has an integer <span>value</span>, a
 *   <span>left</span> child node, and a <span>right</span> child node. A node is
 *   said to be a valid <span>BST</span> node if and only if it satisfies the BST
 *   property: its <span>value</span> is strictly greater than the values of every
 *   node to its left; its <span>value</span> is less than or equal to the values
 *   of every node to its right; and its children nodes are either valid
 *   <span>BST</span> nodes themselves or <span>None</span> / <span>null</span>.
 * </p>
 * <h3>Sample Usage</h3>
 * <pre><span class="CodeEditor-promptComment">// Assume the following BST has already been created:</span>
 *          10
 *        /     \
 *       5      15
 *     /   \   /   \
 *    2     5 13   22
 *  /           \
 * 1            14
 *
 * <span class="CodeEditor-promptComment">// All operations below are performed sequentially.</span>
 * <span class="CodeEditor-promptParameter">insert</span>(12):   10
 *             /     \
 *            5      15
 *          /   \   /   \
 *         2     5 13   22
 *       /        /  \
 *      1        12  14
 *
 * <span class="CodeEditor-promptParameter">remove</span>(10):   12
 *             /     \
 *            5      15
 *          /   \   /   \
 *         2     5 13   22
 *       /           \
 *      1            14
 *
 * <span class="CodeEditor-promptParameter">contains</span>(15): true
 * </pre>
 * </div>
 */
public class BSTConstruction {
    public static void main(String[] args) {
        var root = new BST(10);
        root.left = new BST(5);
        root.left.left = new BST(2);
        root.left.left.left = new BST(1);
        root.left.right = new BST(5);
        root.right = new BST(15);
        root.right.left = new BST(13);
        root.right.left.right = new BST(14);
        root.right.right = new BST(22);

        root.insert(12);
        System.out.println(root.right.left.left.value == 12);

        root.remove(10);
        System.out.println(root.contains(10) == false);
        System.out.println(root.value == 12);

        System.out.println(root.contains(15));
    }

    static class BST {
        public int value;
        public BST left;
        public BST right;

        public BST(int value) {
            this.value = value;
        }

        public BST insert(int value) {
            if (value < this.value) {
                if (left == null) {
                    BST newBST = new BST(value);
                    left = newBST;
                } else {
                    left.insert(value);
                }
            } else {
                if (right == null) {
                    BST newBST = new BST(value);
                    right = newBST;
                } else {
                    right.insert(value);
                }
            }
            return this;
        }

        public boolean contains(int value) {
            if (value < this.value) {
                if (left == null) {
                    return false;
                } else {
                    return left.contains(value);
                }
            } else if (value > this.value) {
                if (right == null) {
                    return false;
                } else {
                    return right.contains(value);
                }
            } else {
                return true;
            }
        }

        public BST remove(int value) {
            remove(value, null);
            return this;
        }

        public void remove(int value, BST parent) {
            if (value < this.value) {
                if (left != null) {
                    left.remove(value, this);
                }
            } else if (value > this.value) {
                if (right != null) {
                    right.remove(value, this);
                }
            } else {
                if (left != null && right != null) {
                    this.value = right.getMinValue();
                    right.remove(this.value, this);
                } else if (parent == null) {
                    if (left != null) {
                        this.value = left.value;
                        right = left.right;
                        left = left.left;
                    } else if (right != null) {
                        this.value = right.value;
                        left = right.left;
                        right = right.right;
                    } else {
                        // This is a single node tree, do nothing.
                    }
                } else if (parent.left == this) {
                    parent.left = left != null ? left : right;
                } else if (parent.right == this) {
                    parent.right = left != null ? left : right;
                }
            }
        }

        public int getMinValue() {
            if (left == null) {
                return this.value;
            } else {
                return left.getMinValue();
            }
        }
    }
}
