package array;

import java.util.Arrays;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] output = new int[2];
        int[] ints = twoNumbersSum(Arrays.copyOf(nums, nums.length), target);
        for(int i = 0; i < nums.length; i++) {
            int first = ints[0];
            int second = ints[1];

            if(nums[i] == first) output[0] = i;
            else if(nums[i] == second) output[1] = i;
        }
        return output;
    }

    private int[] twoNumbersSum(int[] array, int target) {
        Arrays.sort(array);
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            int currentSum = array[left] + array[right];
            if(currentSum == target) {
                return new int[] {array[left],array[right]};
            } else if (currentSum < target) {
                left ++;
            } else if (currentSum > target) {
                right--;
            }
        }
        return new int[0];
    }
}
