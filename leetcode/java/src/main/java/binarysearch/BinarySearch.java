package binarysearch;

/**
 * LC 704 Binary Search.
 * Approach: closed interval [lo, hi], halve each step.
 * Time O(log n), Space O(1).
 */
public class BinarySearch {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
