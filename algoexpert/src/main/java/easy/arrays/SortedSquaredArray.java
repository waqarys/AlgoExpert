package easy.arrays;

/**
 * Sorted Squared Array: given a sorted array (may contain negatives) return the squares in sorted order.
 * Two pointers from both ends fill the result from the back.
 * Time: O(n) | Space: O(n).
 */
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
