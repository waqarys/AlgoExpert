package medium.binarysearchtrees;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a potentially invalid Binary Search Tree (BST)
 *   and returns a boolean representing whether the BST is valid.
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
 * <p>
 *   A BST is valid if and only if all of its nodes are valid
 *   <span>BST</span> nodes.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> =   10
 *        /     \
 *       5      15
 *     /   \   /   \
 *    2     5 13   22
 *  /           \
 * 1            14
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>true</pre>
 * </div>
 */
public class ValidateBST {
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

        System.out.println(validateBst(root));
    }

    public static boolean validateBst(BST tree) {
        return validateBst(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    public static boolean validateBst(BST tree, int minValue, int maxValue) {
        if (tree.value < minValue || tree.value >= maxValue) {
            return false;
        }
        if (tree.left != null && !validateBst(tree.left, minValue, tree.value)) {
            return false;
        }
        if (tree.right != null && !validateBst(tree.right, tree.value, maxValue)) {
            return false;
        }
        return true;
    }

    static class BST {
        public int value;
        public BST left;
        public BST right;

        public BST(int value) {
            this.value = value;
        }
    }
}
