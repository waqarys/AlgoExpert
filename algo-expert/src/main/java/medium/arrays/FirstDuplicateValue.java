package medium.arrays;

import java.util.HashSet;

/**
 * <div class="html">
 * <p>
 *   Given an array of integers between <span>1</span> and <span>n</span>,
 *   inclusive, where <span>n</span> is the length of the array, write a function
 *   that returns the first integer that appears more than once (when the array is
 *   read from left to right).
 * </p>
 * <p>
 *   In other words, out of all the integers that might occur more than once in the
 *   input array, your function should return the one whose first duplicate value
 *   has the minimum index.
 * </p>
 * <p>
 *   If no integer appears more than once, your function should return
 *   <span>-1</span>.
 * </p>
 * <p>Note that you're allowed to mutate the input array.</p>
 * <h3>Sample Input #1</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 2, 3, 3, 4]
 * </pre>
 * <h3>Sample Output #1</h3>
 * <pre>2 <span class="CodeEditor-promptComment">// 2 is the first integer that appears more than once.</span>
 * <span class="CodeEditor-promptComment">// 3 also appears more than once, but the second 3 appears after the second 2.</span>
 * </pre>
 * <h3>Sample Input #2</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 5, 3, 3, 2, 4]
 * </pre>
 * <h3>Sample Output #2</h3>
 * <pre>3 <span class="CodeEditor-promptComment">// 3 is the first integer that appears more than once.</span>
 * <span class="CodeEditor-promptComment">// 2 also appears more than once, but the second 2 appears after the second 3.</span>
 * </pre>
 * </div>
 */
public class FirstDuplicateValue {

    public static void main(String[] args) {
        var input = new int[] {2, 1, 5, 2, 3, 3, 4};
        var expected = 2;
        var actual = firstDuplicateValue(input);
        System.out.println(expected == actual);

        var actual1 = firstDuplicateValue1(input);
        System.out.println(expected == actual1);
    }

    public static int firstDuplicateValue(int[] array) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for (int value : array) {
            if (seen.contains(value)) return value;
            seen.add(value);
        }
        return -1;
    }

    public static int firstDuplicateValue1(int[] array) {
        for (int value : array) {
            int absValue = Math.abs(value);
            if (array[absValue - 1] < 0) return absValue;
            array[absValue - 1] *= -1;
        }
        return -1;
    }
}
