package dp1;

/**
 * LC 70 Climbing Stairs.
 * Approach: Fibonacci recurrence ways(n) = ways(n-1) + ways(n-2) with two variables.
 * Time O(n), Space O(1).
 */
public class ClimbingStairs {
    public int climbStairs(int n) {
        int a = 1, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
