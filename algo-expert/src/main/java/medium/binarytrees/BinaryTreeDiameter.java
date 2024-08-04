package medium.binarytrees;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a Binary Tree and returns its diameter. The
 *   diameter of a binary tree is defined as the length of its longest path, even
 *   if that path doesn't pass through the root of the tree.
 * </p>
 * <p>
 *   A path is a collection of connected nodes in a tree, where no node is
 *   connected to more than two other nodes. The length of a path is the number of
 *   edges between the path's first node and its last node.
 * </p>
 * <p>
 *   Each <span>BinaryTree</span> node has an integer <span>value</span>, a
 *   <span>left</span> child node, and a <span>right</span> child node. Children
 *   nodes can either be <span>BinaryTree</span> nodes themselves or
 *   <span>None</span> / <span>null</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> =        1
 *             /   \
 *            3     2
 *          /   \
 *         7     4
 *        /       \
 *       8         5
 *      /           \
 *     9             6
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>6 <span class="CodeEditor-promptComment">// 9 -&gt; 8 -&gt; 7 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6</span>
 * <span class="CodeEditor-promptComment">// There are 6 edges between the</span>
 * <span class="CodeEditor-promptComment">// first node and the last node</span>
 * <span class="CodeEditor-promptComment">// of this tree's longest path.</span>
 * </pre>
 * </div>
 */
public class BinaryTreeDiameter {
    public static void main(String[] args) {

    }

    static class BinaryTree {
        public int value;
        public BinaryTree left = null;
        public BinaryTree right = null;

        public BinaryTree(int value) {
            this.value = value;
        }
    }

    public int binaryTreeDiameter(BinaryTree tree) {
        return getTreeInfo(tree).diameter;
    }

    public TreeInfo getTreeInfo(BinaryTree tree) {
        if (tree == null) {
            return new TreeInfo(0, 0);
        }

        TreeInfo leftTreeInfo = getTreeInfo(tree.left);
        TreeInfo rightTreeInfo = getTreeInfo(tree.right);

        int longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height;
        int maxDiameterSoFar = Math.max(leftTreeInfo.diameter, rightTreeInfo.diameter);
        int currentDiameter = Math.max(longestPathThroughRoot, maxDiameterSoFar);
        int currentHeight = 1 + Math.max(leftTreeInfo.height, rightTreeInfo.height);

        return new TreeInfo(currentDiameter, currentHeight);
    }

    static class TreeInfo {
        public int diameter;
        public int height;

        public TreeInfo(int diameter, int height) {
            this.diameter = diameter;
            this.height = height;
        }
    }
}
