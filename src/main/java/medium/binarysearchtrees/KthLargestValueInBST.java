package medium.binarysearchtrees;

import java.util.ArrayList;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a Binary Search Tree (BST) and a positive
 *   integer <span>k</span> and returns the kth largest integer contained in the
 *   BST.
 * </p>
 * <p>
 *   You can assume that there will only be integer values in the BST and that
 *   <span>k</span> is less than or equal to the number of nodes in the tree.
 * </p>
 * <p>
 *   Also, for the purpose of this question, duplicate integers will be treated as
 *   distinct values. In other words, the second largest value in a BST containing
 *   values <span>{5, 7, 7}</span> will be <span>7</span>—not <span>5</span>.
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
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">tree</span> =   15
 *        /     \
 *       5      20
 *     /   \   /   \
 *    2     5 17   22
 *  /   \
 * 1     3
 * <span class="CodeEditor-promptParameter">k</span> = 3
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>17</pre>
 * </div>
 */
public class KthLargestValueInBST {

    public static void main(String[] args) {
        BST root = new BST(15);
        root.left = new BST(5);
        root.left.left = new BST(2);
        root.left.left.left = new BST(1);
        root.left.left.right = new BST(3);
        root.left.right = new BST(5);
        root.right = new BST(20);
        root.right.left = new BST(17);
        root.right.right = new BST(22);
        int k = 3;
        int expected = 17;
        var actual = new KthLargestValueInBST().findKthLargestValueInBst(root, k);
        System.out.println(expected == actual);
    }

    static class BST {
        public int value;
        public BST left = null;
        public BST right = null;

        public BST(int value) {
            this.value = value;
        }
    }

    public int findKthLargestValueInBst(BST tree, int k) {
        ArrayList<Integer> sortedNodeValues = new ArrayList<>();
        inOrderTraverse(tree, sortedNodeValues);
        return sortedNodeValues.get(sortedNodeValues.size() - k);
    }

    public void inOrderTraverse(BST node, ArrayList<Integer> sortedNodeValues) {
        if (node == null) return;

        inOrderTraverse(node.left, sortedNodeValues);
        sortedNodeValues.add(node.value);
        inOrderTraverse(node.right, sortedNodeValues);
    }
}
