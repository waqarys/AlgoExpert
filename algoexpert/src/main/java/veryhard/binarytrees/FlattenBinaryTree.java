package veryhard.binarytrees;

import common.BinaryTree;

/**
 * Flatten Binary Tree: rewire the tree in place into a doubly linked list in in-order order (left = prev,
 * right = next); return the leftmost node.
 * Time: O(n) | Space: O(h).
 */
public class FlattenBinaryTree {
    public static BinaryTree flattenBinaryTree(BinaryTree root) { return flatten(root)[0]; }

    /** returns {leftmost, rightmost} of the flattened subtree */
    private static BinaryTree[] flatten(BinaryTree n) {
        BinaryTree leftMost = n, rightMost = n;
        if (n.left != null) {
            BinaryTree[] l = flatten(n.left);
            l[1].right = n; n.left = l[1]; leftMost = l[0];
        }
        if (n.right != null) {
            BinaryTree[] r = flatten(n.right);
            r[0].left = n; n.right = r[0]; rightMost = r[1];
        }
        return new BinaryTree[]{leftMost, rightMost};
    }
}
