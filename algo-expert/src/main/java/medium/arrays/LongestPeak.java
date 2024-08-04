package medium.arrays;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of integers and returns the length of
 *   the longest peak in the array.
 * </p>
 * <p>
 *   A peak is defined as adjacent integers in the array that are <b>strictly</b>
 *   increasing until they reach a tip (the highest value in the peak), at which
 *   point they become <b>strictly</b> decreasing. At least three integers are required to
 *   form a peak.
 * </p>
 * <p>
 *   For example, the integers <span>1, 4, 10, 2</span> form a peak, but the
 *   integers <span>4, 0, 10</span> don't and neither do the integers
 *   <span>1, 2, 2, 0</span>. Similarly, the integers <span>1, 2, 3</span> don't
 *   form a peak because there aren't any strictly decreasing integers after the
 *   <span>3</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>6 <span class="CodeEditor-promptComment">// 0, 10, 6, 5, -1, -3</span>
 * </pre>
 * </div>
 */
public class LongestPeak {
    public static void main(String[] args) {
        var input = new int[] {1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3};
        var expected = 6;
        var actual = longestPeak(input);
        System.out.println(expected == actual);
    }

    public static int longestPeak(int[] array) {
        int longestPeakLength = 0;
        int i =1;
        while (i < array.length - 1) {
            boolean isPeak = array[i - 1] < array[i] && array[i] > array[i + 1];
            if(!isPeak) {
                i += 1;
                continue;
            }

            int leftIdx = i - 2;
            while (leftIdx >= 0 && array[leftIdx] < array[leftIdx + 1]) {
                leftIdx -= 1;
            }

            int rightIdx = i + 2;
            while (rightIdx < array.length && array[rightIdx] < array[rightIdx - 1]) {
                rightIdx += 1;
            }

            int currentPeakLength = rightIdx - leftIdx - 1;
            if(currentPeakLength > longestPeakLength) {
                longestPeakLength = currentPeakLength;
            }
            i = rightIdx;
        }
        return longestPeakLength;
    }
}
