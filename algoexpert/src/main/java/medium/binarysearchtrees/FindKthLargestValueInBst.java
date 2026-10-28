package medium.binarysearchtrees;

import common.BST;

/**
 * Find Kth Largest Value In BST: reverse in-order traversal, stopping after k nodes.
 * Time: O(h + k) | Space: O(h).
 */
public class FindKthLargestValueInBst {
    private static int seen, answer;

    public static synchronized int findKthLargestValueInBst(BST tree, int k) {
        seen = 0; answer = -1;
        walk(tree, k);
        return answer;
    }

    private static void walk(BST n, int k) {
        if (n == null || seen >= k) return;
        walk(n.right, k);
        if (seen < k) { seen++; if (seen == k) { answer = n.value; return; } walk(n.left, k); }
    }
}
