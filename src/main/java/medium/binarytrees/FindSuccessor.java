package medium.binarytrees;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a Binary Tree (where nodes have an additional
 *   pointer to their parent node) as well as a node contained in that tree and
 *   returns the given node's successor.
 * </p>
 * <p>
 *   A node's successor is the next node to be visited (immediately after the given
 *   node) when traversing its tree using the in-order tree-traversal technique. A
 *   node has no successor if it's the last node to be visited in the in-order
 *   traversal.
 * </p>
 * <p>
 *   If a node has no successor, your function should return <span>None</span> /
 *   <span>null</span>.
 * </p>
 * <p>
 *   Each <span>BinaryTree</span> node has an integer <span>value</span>, a
 *   <span>parent</span> node, a <span>left</span> child node, and a
 *   <span>right</span> child node. Children nodes can either be
 *   <span>BinaryTree</span> nodes themselves or <span>None</span> /
 *   <span>null</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> =
 *               1
 *             /   \
 *            2     3
 *          /   \
 *         4     5
 *        /
 *       6
 * <span class="CodeEditor-promptParameter">node</span> = 5
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>1
 * <span class="CodeEditor-promptComment">// This tree's in-order traversal order is:</span>
 * <span class="CodeEditor-promptComment">// 6 -&gt; 4 -&gt; 2 -&gt; 5 -&gt; 1 -&gt; 3 </span>
 * <span class="CodeEditor-promptComment">// 1 comes immediately after 5.</span>
 * </pre>
 * </div>
 */
public class FindSuccessor {

    public static void main(String[] args) {
        BinaryTree root = new BinaryTree(1);
        root.left = new BinaryTree(2);
        root.left.parent = root;
        root.right = new BinaryTree(3);
        root.right.parent = root;
        root.left.left = new BinaryTree(4);
        root.left.left.parent = root.left;
        root.left.right = new BinaryTree(5);
        root.left.right.parent = root.left;
        root.left.left.left = new BinaryTree(6);
        root.left.left.left.parent = root.left.left;
        BinaryTree node = root.left.right;
        BinaryTree expected = root;
        BinaryTree output = new FindSuccessor().findSuccessor(root, node);
        assert (expected == output);
    }

    static class BinaryTree {
        public int value;
        public BinaryTree left = null;
        public BinaryTree right = null;
        public BinaryTree parent = null;

        public BinaryTree(int value) {
            this.value = value;
        }
    }

    public BinaryTree findSuccessor(BinaryTree tree, BinaryTree node) {
        if(node.right != null) return getLeftmostChild(node.right);
        return getRightmostParent(node);
    }

    public BinaryTree getLeftmostChild(BinaryTree node) {
        BinaryTree currentNode = node;
        while (currentNode.left != null) {
            currentNode = currentNode.left;
        }

        return currentNode;
    }

    public BinaryTree getRightmostParent(BinaryTree node) {
        BinaryTree currentNode = node;
        while (currentNode.parent != null && currentNode.parent.right == currentNode) {
            currentNode = currentNode.parent;
        }

        return currentNode.parent;
    }
}
