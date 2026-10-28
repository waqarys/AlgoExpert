package easy.arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * Two Number Sum: given distinct integers and a target, return any pair summing to the target
 * (empty array if none).
 * Time: O(n) | Space: O(n) using a hash set of seen values.
 */
public class TwoNumberSum {
    public static int[] twoNumberSum(int[] array, int target) {
        Set<Integer> seen = new HashSet<>();
        for (int x : array) {
            if (seen.contains(target - x)) return new int[]{target - x, x};
            seen.add(x);
        }
        return new int[0];
    }
}
