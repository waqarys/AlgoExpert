package medium.arrays;

/**
 * Majority Element: an element occurs in more than half the array; find it (Boyer-Moore voting).
 * Time: O(n) | Space: O(1).
 */
public class MajorityElement {
    public static int majorityElement(int[] a) {
        int cand = 0, count = 0;
        for (int x : a) {
            if (count == 0) cand = x;
            count += (x == cand) ? 1 : -1;
        }
        return cand;
    }
}
