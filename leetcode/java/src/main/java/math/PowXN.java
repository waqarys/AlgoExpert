package math;

/**
 * LC 50 Pow(x, n).
 * Approach: iterative binary exponentiation; a long exponent avoids MIN_VALUE overflow.
 * Time O(log n), Space O(1).
 */
public class PowXN {
    public double myPow(double x, int n) {
        long e = n;
        if (e < 0) { x = 1 / x; e = -e; }
        double res = 1;
        while (e > 0) {
            if ((e & 1) == 1) res *= x;
            x *= x;
            e >>= 1;
        }
        return res;
    }
}
