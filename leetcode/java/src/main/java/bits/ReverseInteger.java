package bits;

/**
 * LC 7 Reverse Integer.
 * Approach: pop/push digits with a pre-multiplication overflow check (no 64-bit math).
 * Time O(log x), Space O(1).
 */
public class ReverseInteger {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int d = x % 10;
            x /= 10;
            if (res > Integer.MAX_VALUE / 10 || (res == Integer.MAX_VALUE / 10 && d > 7)) return 0;
            if (res < Integer.MIN_VALUE / 10 || (res == Integer.MIN_VALUE / 10 && d < -8)) return 0;
            res = res * 10 + d;
        }
        return res;
    }
}
