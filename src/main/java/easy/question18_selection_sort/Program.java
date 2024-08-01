package easy.question18_selection_sort;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of integers and returns a sorted
 *   version of that array. Use the Selection Sort algorithm to sort the array.
 * </p>
 * <p>
 *   If you're unfamiliar with Selection Sort, we recommend watching the Conceptual
 *   Overview section of this question's video explanation before starting to code.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [8, 5, 2, 9, 5, 6, 3]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[2, 3, 5, 5, 6, 8, 9]
 * </pre>
 * </div>
 */
public class Program {
    public static void main(String[] args) {
        int[] expected = {2, 3, 5, 5, 6, 8, 9};
        int[] input = {8, 5, 2, 9, 5, 6, 3};
        selectionSort(input);
    }

    public static int[] selectionSort(int[] array) {
        if(array.length == 0){
            return new int[] {};
        }
        int startIdx = 0;
        while (startIdx < array.length - 1) {
            int smallestIdx = startIdx;
            for (int i = startIdx + 1; i < array.length; i++) {
                if(array[smallestIdx] > array[i]) {
                    smallestIdx = i;
                }
            }
            swap(startIdx, smallestIdx, array);
            startIdx++;
        }
        return array;
    }

    public static void swap(int i, int j, int[] array) {
        int temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }
}
