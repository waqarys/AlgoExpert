package bits;

/**
 * LC 190 Reverse Bits.
 * Approach: pop the low bit of n, push it onto res, 32 times.
 * Time O(32), Space O(1).
 */
public class ReverseBits {
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>>= 1;
        }
        return res;
    }
}
