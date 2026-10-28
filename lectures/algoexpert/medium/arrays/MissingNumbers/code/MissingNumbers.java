public class MissingNumbers {
    public static int[] missingNumbers(int[] nums) {
        int n = nums.length + 2;
        long total = (long) n * (n + 1) / 2;
        for (int x : nums) total -= x;
        long avg = total / 2, lowExpected = avg * (avg + 1) / 2, lowActual = 0;
        for (int x : nums) if (x <= avg) lowActual += x;
        int a = (int) (lowExpected - lowActual);
        return new int[]{a, (int) (total - a)};
    }
}
