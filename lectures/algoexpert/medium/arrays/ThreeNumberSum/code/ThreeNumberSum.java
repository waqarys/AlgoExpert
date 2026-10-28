public class ThreeNumberSum {
    public static List<Integer[]> threeNumberSum(int[] array, int target) {
        Arrays.sort(array);
        List<Integer[]> out = new ArrayList<>();
        for (int i = 0; i < array.length - 2; i++) {
            int l = i + 1, r = array.length - 1;
            while (l < r) {
                int s = array[i] + array[l] + array[r];
                if (s == target) { out.add(new Integer[]{array[i], array[l], array[r]}); l++; r--; }
                else if (s < target) l++; else r--;
            }
        }
        return out;
    }
}
