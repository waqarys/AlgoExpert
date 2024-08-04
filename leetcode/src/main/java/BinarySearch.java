public class BinarySearch {

    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while(start < end) {
            int mid = start + (end - start) / 2;
            if(nums[mid] == target) {
                return mid;
            } else if(target < nums[mid]) {
                end = mid;
            } else if(target > nums[mid]) {
                start = mid + 1;
            }
        }

        if(nums[start] == target) {
            return start;
        }
        return -1;
    }
}
