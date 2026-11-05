package bits;

/**
 * LC 371 Sum of Two Integers.
 * Approach: XOR for the sum without carry, AND<<1 for the carry; loop until no carry.
 * Time O(32), Space O(1).
 */
public class SumOfTwoIntegers {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
