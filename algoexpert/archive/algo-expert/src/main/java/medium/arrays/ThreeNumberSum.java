package medium.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a non-empty array of distinct integers and an
 *   integer representing a target sum. The function should find all triplets in
 *   the array that sum up to the target sum and return a two-dimensional array of
 *   all these triplets. The numbers in each triplet should be ordered in ascending
 *   order, and the triplets themselves should be ordered in ascending order with
 *   respect to the numbers they hold.
 * </p>
 * <p>
 *   If no three numbers sum up to the target sum, the function should return an
 *   empty array.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [12, 3, 1, 2, -6, 5, -8, 6]
 * <span class="CodeEditor-promptParameter">targetSum</span> = 0
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
 * </pre>
 * </div>
 */
public class ThreeNumberSum extends Compare {
    public static void main(String[] args) {
        List<Integer[]> expected = new ArrayList<Integer[]>();
        expected.add(new Integer[] {-8, 2, 6});
        expected.add(new Integer[] {-8, 3, 5});
        expected.add(new Integer[] {-6, 1, 5});
        List<Integer[]> output = threeNumberSum(new int[] {12, 3, 1, 2, -6, 5, -8, 6}, 0);
        System.out.println(compare(output, expected));
    }

    public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
        Arrays.sort(array);
        List<Integer[]> triplets = new ArrayList<Integer[]>();
        for (int i = 0; i< array.length - 2; i++) {
            int left = i + 1;
            int right = array.length - 1;
            while (left < right) {
                int currentSum = array[i] + array[left] + array[right];
                if(currentSum == targetSum){
                    Integer[] newTriplet = {array[i], array[left], array[right]};
                    triplets.add(newTriplet);
                    left++;
                    right--;
                } else if (currentSum < targetSum) {
                    left++;
                } else if (currentSum > targetSum) {
                    right--;
                }
            }
        }
        return triplets;
    }
}
