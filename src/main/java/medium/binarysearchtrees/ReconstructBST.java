package medium.binarysearchtrees;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   The pre-order traversal of a Binary Tree is a traversal technique that starts
 *   at the tree's root node and visits nodes in the following order:
 * </p>
 * <ol>
 *   <li>Current node</li>
 *   <li>Left subtree</li>
 *   <li>Right subtree</li>
 * </ol>
 * <p>
 *   Given a non-empty array of integers representing the pre-order traversal of a
 *   Binary Search Tree (BST), write a function that creates the relevant BST and
 *   returns its root node.
 * </p>
 * <p>
 *   The input array will contain the values of BST nodes in the order in which
 *   these nodes would be visited with a pre-order traversal.
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
 * <pre><span class="CodeEditor-promptParameter">preOrderTraversalValues</span> = [10, 4, 2, 1, 5, 17, 19, 18]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>        10
 *       /    \
 *      4      17
 *    /   \      \
 *   2     5     19
 *  /           /
 * 1           18
 * </pre>
 * </div>
 */
public class ReconstructBST {
    public static void main(String[] args) {
        List<Integer> preOrderTraversalValues =
                new ArrayList<Integer>(Arrays.asList(10, 4, 2, 1, 3, 17, 19, 18));
        BST tree = new BST(10);
        tree.left = new BST(4);
        tree.left.left = new BST(2);
        tree.left.left.left = new BST(1);
        tree.left.right = new BST(3);
        tree.right = new BST(17);
        tree.right.right = new BST(19);
        tree.right.right.left = new BST(18);
        List<Integer> expected = getDfsOrder(tree, new ArrayList<Integer>());
        var actual = new ReconstructBST().reconstructBst(preOrderTraversalValues);
        List<Integer> actualValues = getDfsOrder(actual, new ArrayList<Integer>());
        System.out.println(expected.equals(actualValues));
    }

    public static List<Integer> getDfsOrder(BST node, List<Integer> values) {
        values.add(node.value);
        if (node.left != null) {
            getDfsOrder(node.left, values);
        }
        if (node.right != null) {
            getDfsOrder(node.right, values);
        }
        return values;
    }

    static class BST {
        public int value;
        public BST left = null;
        public BST right = null;

        public BST(int value) {
            this.value = value;
        }
    }

    public BST reconstructBst(List<Integer> preOrderTraversalValues) {
        if(preOrderTraversalValues.size() == 0) {
            return null;
        }

        int currentValue = preOrderTraversalValues.get(0);
        int rightSubTreeRootIdx = preOrderTraversalValues.size();

        for (int idx = 1; idx < preOrderTraversalValues.size(); idx++) {
            int value = preOrderTraversalValues.get(idx);
            if (value >= currentValue) {
                rightSubTreeRootIdx = idx;
                break;
            }
        }

        BST leftSubtree = reconstructBst(preOrderTraversalValues.subList(1, rightSubTreeRootIdx));
        BST rightSubtree =
                reconstructBst(
                        preOrderTraversalValues.subList(rightSubTreeRootIdx, preOrderTraversalValues.size())
                );
        BST bst = new BST(currentValue);
        bst.left = leftSubtree;
        bst.right = rightSubtree;

        return bst;
    }
}
