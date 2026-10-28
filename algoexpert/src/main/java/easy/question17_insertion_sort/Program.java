package easy.question17_insertion_sort;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of integers and returns a sorted
 *   version of that array. Use the Insertion Sort algorithm to sort the array.
 * </p>
 * <p>
 *   If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
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
        compare(insertionSort(input), expected);
    }

    public static boolean compare(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) {
            return false;
        }
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }

    public static int[] insertionSort(int[] array) {
        if(array.length == 0) {
            return new int[] {};
        }
        for (int i = 1; i < array.length; i++) {
            int j = i;
            while (j > 0 && array[j] < array[j - 1]) {
                swap(j, j -1, array);
                j -= 1;
            }
        }
        return array;
    }

    public static void swap(int i, int j, int[] array) {
        int temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }

}
