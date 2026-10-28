package easy.recursion;

/**
 * Nth Fibonacci: F(1)=0, F(2)=1. Iterative with two variables.
 * Time: O(n) | Space: O(1).
 */
public class NthFibonacci {
    public static int getNthFib(int n) {
        int a = 0, b = 1;
        if (n == 1) return 0;
        for (int i = 3; i <= n; i++) { int c = a + b; a = b; b = c; }
        return b;
    }
}
