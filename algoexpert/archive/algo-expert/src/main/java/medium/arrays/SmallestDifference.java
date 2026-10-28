package medium.arrays;

import java.util.Arrays;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in two non-empty arrays of integers, finds the
 *   pair of numbers (one from each array) whose absolute difference is closest to
 *   zero, and returns an array containing these two numbers, with the number from
 *   the first array in the first position.
 * </p>
 * <p>
 *   Note that the absolute difference of two integers is the distance between
 *   them on the real number line. For example, the absolute difference of -5 and 5
 *   is 10, and the absolute difference of -5 and -4 is 1.
 * </p>
 * <p>
 *   You can assume that there will only be one pair of numbers with the smallest
 *   difference.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">arrayOne</span> = [-1, 5, 10, 20, 28, 3]
 * <span class="CodeEditor-promptParameter">arrayTwo</span> = [26, 134, 135, 15, 17]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[28, 26]</pre>
 * </div>
 */
public class SmallestDifference {
    public static void main(String[] args) {
        int[] expected = {28, 26};
        var result = Arrays.equals(
                smallestDifference(
                        new int[] {-1, 5, 10, 20, 28, 3}, new int[] {26, 134, 135, 15, 17}),
                expected);
        System.out.println(result);
    }

    public static int[] smallestDifference(int[] arrayOne, int[] arrayTwo) {
        Arrays.sort(arrayOne);
        Arrays.sort(arrayTwo);
        int idxOne = 0;
        int idxTwo = 0;
        int smallest = Integer.MAX_VALUE;
        int current = Integer.MAX_VALUE;
        int[] smallestPair = new int[2];
        while (idxOne < arrayOne.length && idxTwo < arrayTwo.length) {
            int firstNum = arrayOne[idxOne];
            int secondNum = arrayTwo[idxTwo];
            if (firstNum < secondNum) {
                current = secondNum - firstNum;
                idxOne++;
            } else if (secondNum < firstNum) {
                current = firstNum - secondNum;
                idxTwo++;
            } else {
                return new int[] {firstNum, secondNum};
            }
            if (smallest > current) {
                smallest = current;
                smallestPair = new int[] {firstNum, secondNum};
            }
        }
        return smallestPair;
    }
}
