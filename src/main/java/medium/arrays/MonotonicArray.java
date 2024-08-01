package medium.arrays;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of integers and returns a boolean
 *   representing whether the array is monotonic.
 * </p>
 * <p>
 *   An array is said to be monotonic if its elements, from left to right, are
 *   entirely non-increasing or entirely non-decreasing.
 * </p>
 * <p>
 *   Non-increasing elements aren't necessarily exclusively decreasing; they simply
 *   don't increase. Similarly, non-decreasing elements aren't necessarily
 *   exclusively increasing; they simply don't decrease.
 * </p>
 * <p>Note that empty arrays and arrays of one element are monotonic.</p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>true
 * </pre>
 * </div>
 */
public class MonotonicArray {
    public static void main(String[] args) {
        var array = new int[] {-1, -5, -10, -1100, -1100, -1101, -1102, -9001};
        var expected = true;
        var actual = isMonotonic(array);
        System.out.println(expected == actual);
    }

    public static boolean isMonotonic(int[] array) {
        var isNonDecreasing = true;
        var isNonIncreasing = true;
        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[i - 1]) {
                isNonDecreasing = false;
            }
            if (array[i] > array[i - 1]) {
                isNonIncreasing = false;
            }
        }
        return isNonDecreasing || isNonIncreasing;
    }
}
