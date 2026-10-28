public class ZeroSumSubarray {
    public static boolean zeroSumSubarray(int[] nums) {
        Set<Long> seen = new HashSet<>();
        seen.add(0L);
        long sum = 0;
        for (int n : nums) { sum += n; if (!seen.add(sum)) return true; }
        return false;
    }
}
