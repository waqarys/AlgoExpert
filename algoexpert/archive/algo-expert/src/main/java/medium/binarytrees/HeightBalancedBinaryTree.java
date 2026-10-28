package medium.binarytrees;

/**
 * <div class="html">
 * <p>
 *   You're given the root node of a Binary Tree. Write a function that returns
 *   <span>true</span> if this Binary Tree is height balanced and
 *   <span>false</span> if it isn't.
 * </p>
 * <p>
 *   A Binary Tree is height balanced if for each node in the tree, the difference
 *   between the height of its left subtree and the height of its right subtree is
 *   at most <span>1</span>.
 * </p>
 * <p>
 *   Each <span>BinaryTree</span> node has an integer <span>value</span>, a
 *   <span>left</span> child node, and a <span>right</span> child node. Children
 *   nodes can either be <span>BinaryTree</span> nodes themselves or
 *   <span>None</span> / <span>null</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> = 1
 *      /   \
 *     2     3
 *   /   \     \
 *  4     5     6
 *      /   \
 *     7     8
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>true
 * </pre>
 * </div>
 */
public class HeightBalancedBinaryTree {

    public static void main(String[] args) {
        BinaryTree root = new BinaryTree(1);
        root = new BinaryTree(1);
        root.left = new BinaryTree(2);
        root.right = new BinaryTree(3);
        root.left.left = new BinaryTree(4);
        root.left.right = new BinaryTree(5);
        root.right.right = new BinaryTree(6);
        root.left.right.left = new BinaryTree(7);
        root.left.right.right = new BinaryTree(8);
        boolean expected = true;
        var actual = new HeightBalancedBinaryTree().heightBalancedBinaryTree(root);
        System.out.println(expected == actual);
    }

    static class BinaryTree {
        public int value;
        public BinaryTree left = null;
        public BinaryTree right = null;

        public BinaryTree(int value) {
            this.value = value;
        }
    }

    static class TreeInfo {
        public boolean isBalanced;
        public int height;

        public TreeInfo(boolean isBalanced, int height) {
            this.isBalanced = isBalanced;
            this.height = height;
        }
    }

    public boolean heightBalancedBinaryTree(BinaryTree tree) {
        TreeInfo treeInfo = getTreeInfo(tree);
        return treeInfo.isBalanced;
    }

    public TreeInfo getTreeInfo(BinaryTree node){
        if (node == null) {
            return new TreeInfo(true, -1);
        }

        TreeInfo leftSubtreeInfo = getTreeInfo(node.left);
        TreeInfo rightSubtreeInfo = getTreeInfo(node.right);

        boolean isBalanced =
                leftSubtreeInfo.isBalanced
                        && rightSubtreeInfo.isBalanced
                        && Math.abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1;

        int height = Math.max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1;
        return new TreeInfo(isBalanced, height);
    }
}
