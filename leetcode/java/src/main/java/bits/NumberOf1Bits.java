package bits;

/**
 * LC 191 Number of 1 Bits.
 * Approach: Brian Kernighan's trick, n &= n - 1 clears the lowest set bit.
 * Time O(set bits), Space O(1).
 */
public class NumberOf1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) { n &= n - 1; count++; }
        return count;
    }
}
