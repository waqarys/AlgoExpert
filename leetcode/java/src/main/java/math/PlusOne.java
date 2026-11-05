package math;

/**
 * LC 66 Plus One.
 * Approach: propagate the carry from the right; all nines -> new leading 1.
 * Time O(n), Space O(1) (O(n) for all nines).
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) { digits[i]++; return digits; }
            digits[i] = 0;
        }
        int[] res = new int[digits.length + 1];
        res[0] = 1;
        return res;
    }
}
