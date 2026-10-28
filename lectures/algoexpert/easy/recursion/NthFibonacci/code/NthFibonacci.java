public class NthFibonacci {
    public static int getNthFib(int n) {
        int a = 0, b = 1;
        if (n == 1) return 0;
        for (int i = 3; i <= n; i++) { int c = a + b; a = b; b = c; }
        return b;
    }
}
