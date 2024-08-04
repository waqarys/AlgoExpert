package medium.binarysearchtrees;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   Write three functions that take in a Binary Search Tree (BST) and an empty
 *   array, traverse the BST, add its nodes' values to the input array, and return
 *   that array. The three functions should traverse the BST using the in-order,
 *   pre-order, and post-order tree-traversal techniques, respectively.
 * </p>
 * <p>
 *   If you're unfamiliar with tree-traversal techniques, we recommend watching the
 *   Conceptual Overview section of this question's video explanation before
 *   starting to code.
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
 * <pre><span class="CodeEditor-promptParameter">tree</span> =   10
 *        /     \
 *       5      15
 *     /   \       \
 *    2     5       22
 *  /
 * 1
 * <span class="CodeEditor-promptParameter">array</span> = []
 * </pre>
 * <h3>Sample Output</h3>
 * <pre><span class="CodeEditor-promptParameter">inOrderTraverse</span>: [1, 2, 5, 5, 10, 15, 22] <span class="CodeEditor-promptComment">// where the array is the input array</span>
 * <span class="CodeEditor-promptParameter">preOrderTraverse</span>: [10, 5, 2, 1, 5, 15, 22] <span class="CodeEditor-promptComment">// where the array is the input array</span>
 * <span class="CodeEditor-promptParameter">postOrderTraverse</span>: [1, 2, 5, 5, 22, 15, 10] <span class="CodeEditor-promptComment">// where the array is the input array</span>
 * </pre>
 * </div>
 */
public class BSTTraversal {

    public static void main(String[] args) {
        var root = new BST(10);
        root.left = new BST(5);
        root.left.left = new BST(2);
        root.left.left.left = new BST(1);
        root.left.right = new BST(5);
        root.right = new BST(15);
        root.right.right = new BST(22);

        List<Integer> inOrder = Arrays.asList(new Integer[] {1, 2, 5, 5, 10, 15, 22});
        List<Integer> preOrder = Arrays.asList(new Integer[] {10, 5, 2, 1, 5, 15, 22});
        List<Integer> postOrder = Arrays.asList(new Integer[] {1, 2, 5, 5, 22, 15, 10});

        System.out.println(inOrderTraverse(root, new ArrayList<Integer>()).equals(inOrder));
        System.out.println(preOrderTraverse(root, new ArrayList<Integer>()).equals(preOrder));
        System.out.println(postOrderTraverse(root, new ArrayList<Integer>()).equals(postOrder));
    }

    public static List<Integer> inOrderTraverse(BST tree, List<Integer> array) {
        if (tree.left != null) {
            inOrderTraverse(tree.left, array);
        }
        array.add(tree.value);
        if (tree.right != null) {
            inOrderTraverse(tree.right, array);
        }
        return array;
    }

    public static List<Integer> preOrderTraverse(BST tree, List<Integer> array) {
        array.add(tree.value);
        if (tree.left != null) {
            preOrderTraverse(tree.left, array);
        }
        if (tree.right != null) {
            preOrderTraverse(tree.right, array);
        }
        return array;
    }

    public static List<Integer> postOrderTraverse(BST tree, List<Integer> array) {
        if (tree.left != null) {
            postOrderTraverse(tree.left, array);
        }
        if (tree.right != null) {
            postOrderTraverse(tree.right, array);
        }
        array.add(tree.value);
        return array;
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
