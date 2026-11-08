package bits;

/**
 * LC 268 Missing Number.
 * Approach: XOR all indices and values; the unmatched number remains.
 * Time O(n), Space O(1).
 */
public class MissingNumber {
    public int missingNumber(int[] nums) {
        int x = nums.length;
        for (int i = 0; i < nums.length; i++) x ^= i ^ nums[i];
        return x;
    }
}
