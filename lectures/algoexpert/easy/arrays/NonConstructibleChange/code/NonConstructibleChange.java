public class NonConstructibleChange {
    public static int nonConstructibleChange(int[] coins) {
        Arrays.sort(coins);
        int reach = 0;
        for (int c : coins) {
            if (c > reach + 1) break;
            reach += c;
        }
        return reach + 1;
    }
}
