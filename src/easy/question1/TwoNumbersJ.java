package easy.question1;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoNumbersJ {
    public static void main(String[] args) {
        int[] result = twoNumbersSum(new int[]{3, 5, -4, 8, 11, 1, -1, 6}, 10);
        for(int r: result){
            System.out.print(r + ", ");
        }
    }

    public static int[] twoNumbersSum(int[] array, int target){
        Arrays.sort(array);
        int left = 0;
        int right = array.length - 1;
        while(left < right){
            int currentSum = array[left] + array[right];
            if(currentSum == target){
                return new int[] {array[left], array[right]};
            } else if (currentSum < target){
                left++;
            } else if (currentSum > target){
                right++;
            }
        }
        return new int[0];
    }

    public static int[] twoNumberSum1(int[] array, int targetSum) {
        // Write your code here.
        for(int i : array){
            Map<Integer, Integer> map = new HashMap<>();
            if(map.containsKey(targetSum - i)){
                return new int[]{i, targetSum - i};
            }
            else {
                map.put(i, targetSum-i);
            }
        }
        return new int[0];
    }
}
