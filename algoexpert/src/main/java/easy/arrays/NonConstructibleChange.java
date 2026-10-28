package easy.arrays;

import java.util.Arrays;

/**
 * Non-Constructible Change: given positive coin values, find the minimum amount that cannot be formed.
 * Sort; if the next coin exceeds (reachable + 1), reachable + 1 is the answer.
 * Time: O(n log n) | Space: O(1) (in-place sort).
 */
public class NonConstructibleChange {
    public static int nonConstructibleChange(int[] coins) {
        Arrays.sort(coins);
        int reach = 0;
        for (int c : coins) {
            if (c > reach + 1) break;
            reach += c;
        }
        return reach + 1;
    }
}
