package bits;

/**
 * LC 338 Counting Bits.
 * Approach: DP bits[i] = bits[i >> 1] + (i & 1).
 * Time O(n), Space O(n).
 */
public class CountingBits {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];
        for (int i = 1; i <= n; i++) bits[i] = bits[i >> 1] + (i & 1);
        return bits;
    }
}
