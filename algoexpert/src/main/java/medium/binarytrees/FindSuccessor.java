package medium.binarytrees;

import common.BinaryTree;

/**
 * Find Successor: nodes have parent pointers; return the in-order successor of `node` (or null).
 * Time: O(h) | Space: O(1).
 */
public class FindSuccessor {
    public static BinaryTree findSuccessor(BinaryTree tree, BinaryTree node) {
        if (node.right != null) {
            BinaryTree c = node.right;
            while (c.left != null) c = c.left;
            return c;
        }
        BinaryTree c = node;
        while (c.parent != null && c.parent.right == c) c = c.parent;
        return c.parent;
    }
}
