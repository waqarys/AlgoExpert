package easy.binarysearchtrees;

import common.BST;

/**
 * Find Closest Value In BST: return the value in the BST closest to the target (assume one answer).
 * Iteratively walk down, pruning half the tree each step.
 * Time: O(log n) avg, O(n) worst | Space: O(1).
 */
public class FindClosestValueInBst {
    public static int findClosestValueInBst(BST tree, int target) {
        int closest = tree.value;
        BST cur = tree;
        while (cur != null) {
            if (Math.abs(target - cur.value) < Math.abs(target - closest)) closest = cur.value;
            if (target < cur.value) cur = cur.left;
            else if (target > cur.value) cur = cur.right;
            else break;
        }
        return closest;
    }
}
