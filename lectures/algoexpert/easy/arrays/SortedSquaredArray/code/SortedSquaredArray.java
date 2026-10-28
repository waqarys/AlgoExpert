public class SortedSquaredArray {
    public static int[] sortedSquaredArray(int[] array) {
        int[] out = new int[array.length];
        int l = 0, r = array.length - 1;
        for (int k = array.length - 1; k >= 0; k--) {
            if (Math.abs(array[l]) > Math.abs(array[r])) { out[k] = array[l] * array[l]; l++; }
            else { out[k] = array[r] * array[r]; r--; }
        }
        return out;
    }
}
