package easy.question12_fibonacci;

public class Solution3 {
    public static void main(String[] args) {
        System.out.println(getNthFib(10));
    }

    public static int getNthFib(int n) {
        int[] lastTwo = {0, 1};
        int counter = 3;
        while (counter <= n) {
            int nextFib = lastTwo[0] + lastTwo[1];
            lastTwo[0] = lastTwo[1];
            lastTwo[1] = nextFib;
            counter++;
        }
        return n > 1 ? lastTwo[1] : lastTwo[0];
    }
}
