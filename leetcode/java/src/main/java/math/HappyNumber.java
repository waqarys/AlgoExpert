package math;

/**
 * LC 202 Happy Number.
 * Approach: Floyd's cycle detection on the digit-square-sum sequence.
 * Time O(log n), Space O(1).
 */
public class HappyNumber {
    public boolean isHappy(int n) {
        int slow = n, fast = next(n);
        while (fast != 1 && slow != fast) {
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast == 1;
    }

    private int next(int n) {
        int s = 0;
        while (n > 0) { int d = n % 10; s += d * d; n /= 10; }
        return s;
    }
}
