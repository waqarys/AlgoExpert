package medium.arrays;

import java.util.*;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a non-empty array of arbitrary intervals,
 *   merges any overlapping intervals, and returns the new intervals in no
 *   particular order.
 * </p>
 * <p>
 *   Each interval <span>interval</span> is an array of two integers, with
 *   <span>interval[0]</span> as the start of the interval and
 *   <span>interval[1]</span> as the end of the interval.
 * </p>
 * <p>
 *   Note that back-to-back intervals aren't considered to be overlapping. For
 *   example, <span>[1, 5]</span> and <span>[6, 7]</span> aren't overlapping;
 *   however, <span>[1, 6]</span> and <span>[6, 7]</span> <i>are</i> indeed
 *   overlapping.
 * </p>
 * <p>
 *   Also note that the start of any particular interval will always be less than
 *   or equal to the end of that interval.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">intervals</span> = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[[1, 2], [3, 8], [9, 10]]
 * <span class="CodeEditor-promptComment">// Merge the intervals [3, 5], [4, 7], and [6, 8].</span>
 * <span class="CodeEditor-promptComment">// The intervals could be ordered differently.</span>
 * </pre>
 * </div>
 */
public class MergeOverlappingIntervals {
    public static void main(String[] args) {
        int[][] intervals =
                new int[][] {
                        {1, 2},
                        {3, 5},
                        {4, 7},
                        {6, 8},
                        {9, 10}
                };
        int[][] expected =
                new int[][] {
                        {1, 2},
                        {3, 8},
                        {9, 10}
                };
        int[][] actual = mergeOverlappingIntervals(intervals);
        for (int i = 0; i < actual.length; i++) {
            for (int j = 0; j < actual[i].length; j++) {
                System.out.println(expected[i][j] == actual[i][j]);
            }
        }
    }

    public static int[][] mergeOverlappingIntervals(int[][] intervals) {
        int[][] sortedIntervals = intervals.clone();
        Arrays.sort(sortedIntervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> mergedIntervals = new ArrayList<>();
        int[] currentInterval = sortedIntervals[0];
        mergedIntervals.add(currentInterval);

        for (int[] nextInterval : sortedIntervals) {
            int currentIntervalEnd = currentInterval[1];
            int nextIntervalStart = nextInterval[0];
            int nextIntervalEnd = nextInterval[1];

            if (currentIntervalEnd >= nextIntervalStart) {
                currentInterval[1] = Math.max(currentIntervalEnd, nextIntervalEnd);
            } else {
                currentInterval = nextInterval;
                mergedIntervals.add(currentInterval);
            }
        }
        return mergedIntervals.toArray(new int[mergedIntervals.size()][]);
    }
}
