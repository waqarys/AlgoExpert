package easy.question14_binary_search;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a sorted array of integers as well as a target
 *   integer. The function should use the Binary Search algorithm to determine if
 *   the target integer is contained in the array and should return its index if it
 *   is, otherwise <span>-1</span>.
 * </p>
 * <p>
 *   If you're unfamiliar with Binary Search, we recommend watching the Conceptual
 *   Overview section of this question's video explanation before starting to code.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
 * <span class="CodeEditor-promptParameter">target</span> = 33
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>3
 * </pre>
 * </div>
 */

public class Program {
    public static void main(String[] args) {
        System.out.println(binarySearch(new int[] {0, 1, 21, 33, 45, 45, 61, 71, 72, 73}, 33) == 3);
    }

    public static int binarySearch(int[] array, int target) {
        return binarySearch(array, target, 0, array.length - 1);
    }

    public static int binarySearch(int[] array, int target, int left, int right) {
        if (left > right) return -1;
        int middle = (left + right) / 2;
        int possibleMatch = array[middle];
        if (target == possibleMatch) {
            return middle;
        } else if (target < possibleMatch) {
            return binarySearch(array, target, left, middle - 1);
        } else {
            return binarySearch(array, target, middle + 1, right);
        }
    }
}
