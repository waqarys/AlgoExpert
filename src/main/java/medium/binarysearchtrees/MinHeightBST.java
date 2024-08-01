package medium.binarysearchtrees;

import java.util.*;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a non-empty sorted array of distinct integers,
 *   constructs a BST from the integers, and returns the root of the BST.
 * </p>
 * <p>
 *   The function should minimize the height of the BST.
 * </p>
 * <p>
 *   You've been provided with a <span>BST</span> class that you'll have to use to
 *   construct the BST.
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
 * <p>
 *   Note that the <span>BST</span> class already has an <span>insert</span> method
 *   which you can use if you want.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 5, 7, 10, 13, 14, 15, 22]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>         10
 *        /     \
 *       2      14
 *     /   \   /   \
 *    1     5 13   15
 *           \       \
 *            7      22
 * <span class="CodeEditor-promptComment">// This is one example of a BST with min height</span>
 * <span class="CodeEditor-promptComment">// that you could create from the input array.</span>
 * <span class="CodeEditor-promptComment">// You could create other BSTs with min height</span>
 * <span class="CodeEditor-promptComment">// from the same array; for example:</span>
 *          10
 *        /     \
 *       5      15
 *     /   \   /   \
 *    2     7 13   22
 *  /           \
 * 1            14
 * </pre>
 * </div>
 */
public class MinHeightBST {
    public static void main(String[] args) {
        List<Integer> array = Arrays.asList(1, 2, 5, 7, 10, 13, 14, 15, 22);
        var tree = minHeightBst(array);

        System.out.println(validateBst(tree));
        System.out.println(4 == getTreeHeight(tree));

        var inOrder = inOrderTraverse(tree, new ArrayList<Integer>());
        List<Integer> expected = Arrays.asList(1, 2, 5, 7, 10, 13, 14, 15, 22);
        System.out.println(expected.equals(inOrder));
    }

    public static BST minHeightBst(List<Integer> array) {
        return constructMinHeightBst(array, null, 0, array.size() - 1);
    }

    public static BST constructMinHeightBst(List<Integer> array, BST bst, int startIdx, int endIdx) {
        if (endIdx < startIdx) return null;
        int midIdx = (startIdx + endIdx) / 2;
        int valueToAdd = array.get(midIdx);
        if (bst == null) {
            bst = new BST(valueToAdd);
        } else {
            bst.insert(valueToAdd);
        }
        constructMinHeightBst(array, bst, startIdx, midIdx - 1);
        constructMinHeightBst(array, bst, midIdx + 1, endIdx);
        return bst;
    }

    static class BST {
        public int value;
        public BST left;
        public BST right;

        public BST(int value) {
            this.value = value;
            left = null;
            right = null;
        }

        public void insert(int value) {
            if (value < this.value) {
                if (left == null) {
                    left = new BST(value);
                } else {
                    left.insert(value);
                }
            } else {
                if (right == null) {
                    right = new BST(value);
                } else {
                    right.insert(value);
                }
            }
        }
    }

    static boolean validateBst(BST tree) {
        return validateBst(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    static boolean validateBst(BST tree, int minValue, int maxValue) {
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

    static List<Integer> inOrderTraverse(BST tree, List<Integer> array) {
        if (tree.left != null) {
            inOrderTraverse(tree.left, array);
        }
        array.add(tree.value);
        if (tree.right != null) {
            inOrderTraverse(tree.right, array);
        }
        return array;
    }

    static int getTreeHeight(BST tree) {
        return getTreeHeight(tree, 0);
    }

    static int getTreeHeight(BST tree, int height) {
        if (tree == null) return height;
        int leftTreeHeight = getTreeHeight(tree.left, height + 1);
        int rightTreeHeight = getTreeHeight(tree.right, height + 1);
        return Math.max(leftTreeHeight, rightTreeHeight);
    }
}
