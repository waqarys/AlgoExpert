public class BinarySearch {
    public static int binarySearch(int[] array, int target) {
        int lo = 0, hi = array.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (array[mid] == target) return mid;
            if (array[mid] < target) lo = mid + 1; else hi = mid - 1;
        }
        return -1;
    }
}
