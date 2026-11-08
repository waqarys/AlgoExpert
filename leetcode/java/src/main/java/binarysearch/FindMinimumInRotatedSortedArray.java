package binarysearch;

/**
 * LC 153 Find Minimum in Rotated Sorted Array.
 * Approach: compare mid with hi; the minimum is in the unsorted half.
 * Time O(log n), Space O(1).
 */
public class FindMinimumInRotatedSortedArray {
    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else hi = mid;
        }
        return nums[lo];
    }
}
