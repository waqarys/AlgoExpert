package medium.binarytrees;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a Binary Tree and inverts it. In other words,
 *   the function should swap every left node in the tree for its corresponding
 *   right node.
 * </p>
 * <p>
 *   Each <span>BinaryTree</span> node has an integer <span>value</span>, a
 *   <span>left</span> child node, and a <span>right</span> child node. Children
 *   nodes can either be <span>BinaryTree</span> nodes themselves or
 *   <span>None</span> / <span>null</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> =    1
 *        /     \
 *       2       3
 *     /   \   /   \
 *    4     5 6     7
 *  /   \
 * 8     9
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>       1
 *     /     \
 *    3       2
 *  /   \   /   \
 * 7     6 5     4
 *             /   \
 *            9     8
 * </pre>
 * </div>
 */
public class InvertBinaryTree {

    public static void main(String[] args) {
    }

    public static void invertBinaryTree(BinaryTree tree) {
        if (tree == null) {
            return;
        }
        swapLeftAndRight(tree);
        invertBinaryTree(tree.left);
        invertBinaryTree(tree.right);
    }

    private static void swapLeftAndRight(BinaryTree tree) {
        BinaryTree left = tree.left;
        tree.left = tree.right;
        tree.right = left;
    }

    static class BinaryTree {
        public int value;
        public BinaryTree left;
        public BinaryTree right;

        public BinaryTree(int value) {
            this.value = value;
        }
    }
}
