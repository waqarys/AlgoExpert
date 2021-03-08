package easy.question6_sorted_square_array;

/**
 *
 * Write a function that takes in a non-empty array of integers that are sorted
 * in ascending order and returns a new array of the same length with the squares
 * of the original integers also sorted in ascending order.
 * e.g.,
 * input: [-3, 1, 2]
 * output: [1, 4, 9]
 */
public class SortedSquareArray2 {
    public static void main(String[] args) {
        var input = new int[] {1, 2, 3, 5, 6, 8, 9};
        var expected = new int[] {1, 4, 9, 25, 36, 64, 81};
        var actual = new SortedSquareArray2().sortedSquaredArray(input);
        for (int i = 0; i < expected.length; i++) {
            System.out.println(expected[i] == actual[i]);
        }
    }

    public int[] sortedSquaredArray(int[] array) {
        int[] sortedSquares = new int[array.length];
        int smallerValueIdx = 0;
        int largerValueIdx = array.length - 1;
        for(int idx = array.length - 1; idx >= 0; idx--){
            int smallerValue = array[smallerValueIdx];
            int largerValue = array[largerValueIdx];
            if (Math.abs(smallerValue) > Math.abs(largerValue)) {
                sortedSquares[idx] = smallerValue * smallerValue;
                smallerValueIdx++;
            } else {
                sortedSquares[idx] = largerValue * largerValue;
                largerValueIdx--;
            }
        }
        return sortedSquares;
    }
}
