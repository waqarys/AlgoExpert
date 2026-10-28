package medium.dynamicprogramming;

/**
 * Max Subset Sum No Adjacent: max sum of positive ints with no two chosen elements adjacent.
 * Time: O(n) | Space: O(1).
 */
public class MaxSubsetSumNoAdjacent {
    public static int maxSubsetSumNoAdjacent(int[] a) {
        int prev = 0, cur = 0;
        for (int x : a) { int next = Math.max(cur, prev + x); prev = cur; cur = next; }
        return cur;
    }
}
