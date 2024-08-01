package medium.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   You're given an array of integers and an integer. Write a function that moves
 *   all instances of that integer in the array to the end of the array and returns
 *   the array.
 * </p>
 * <p>
 *   The function should perform this in place (i.e., it should mutate the input
 *   array) and doesn't need to maintain the order of the other integers.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 1, 2, 2, 2, 3, 4, 2]
 * <span class="CodeEditor-promptParameter">toMove</span> = 2
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[1, 3, 4, 2, 2, 2, 2, 2] <span class="CodeEditor-promptComment">// the numbers 1, 3, and 4 could be ordered differently</span>
 * </pre>
 * </div>
 */
public class MoveElementToEnd {

    public static void main(String[] args) {
        List<Integer> array = new ArrayList<Integer>(Arrays.asList(2, 1, 2, 2, 2, 3, 4, 2));
        int toMove = 2;
        List<Integer> expectedStart = new ArrayList<Integer>(Arrays.asList(1, 3, 4));
        List<Integer> expectedEnd = new ArrayList<Integer>(Arrays.asList(2, 2, 2, 2, 2));
        List<Integer> output = moveElementToEnd(array, toMove);
        List<Integer> outputStart = output.subList(0, 3);
        outputStart.sort(Comparator.naturalOrder());
        List<Integer> outputEnd = output.subList(3, output.size());
        System.out.println(outputStart.equals(expectedStart));
        System.out.println(outputEnd.equals(expectedEnd));
    }

    public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {
        int i = 0;
        int j = array.size() - 1;
        while(i < j) {
            while (i < j && array.get(j) == toMove) j--;
            if (array.get(i) == toMove) swap(i, j, array);
            i++;
        }
        return array;
    }

    public static void swap(int i, int j, List<Integer> array) {
        int temp = array.get(j);
        array.set(j, array.get(i));
        array.set(i, temp);
    }
}
