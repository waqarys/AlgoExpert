public class TwoNumberSum {
    public static int[] twoNumberSum(int[] array, int target) {
        Set<Integer> seen = new HashSet<>();
        for (int x : array) {
            if (seen.contains(target - x)) return new int[]{target - x, x};
            seen.add(x);
        }
        return new int[0];
    }
}
