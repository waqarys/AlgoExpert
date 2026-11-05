package bits;

/**
 * LC 136 Single Number.
 * Approach: XOR all values; pairs cancel.
 * Time O(n), Space O(1).
 */
public class SingleNumber {
    public int singleNumber(int[] nums) {
        int x = 0;
        for (int v : nums) x ^= v;
        return x;
    }
}
