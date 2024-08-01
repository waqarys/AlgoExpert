package medium.dynamicprogramming;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of positive integers and returns the
 *   maximum sum of non-adjacent elements in the array.
 * </p>
 * <p>If the input array is empty, the function should return <span>0</span>.</p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [75, 105, 120, 75, 90, 135]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>330 <span class="CodeEditor-promptComment">// 75 + 120 + 135</span>
 * </pre>
 * </div>
 */
public class MaxSubsetSumNoAdjacent {
    public static void main(String[] args) {
        int[] input = {75, 105, 120, 75, 90, 135};
        System.out.println(maxSubsetSumNoAdjacent(input) == 330);
    }

    public static int maxSubsetSumNoAdjacent(int[] array) {
        if (array.length == 0) {
            return 0;
        } else if (array.length == 1) {
            return array[0];
        }
        int second = array[0];
        int first = Math.max(array[0], array[1]);
        for (int i = 2; i < array.length; i++) {
            int current = Math.max(first, second + array[i]);
            second = first;
            first = current;
        }
        return first;
    }
}
