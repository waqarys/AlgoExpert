public class MaxSubsetSumNoAdjacent {
    public static int maxSubsetSumNoAdjacent(int[] a) {
        int prev = 0, cur = 0;
        for (int x : a) { int next = Math.max(cur, prev + x); prev = cur; cur = next; }
        return cur;
    }
}
