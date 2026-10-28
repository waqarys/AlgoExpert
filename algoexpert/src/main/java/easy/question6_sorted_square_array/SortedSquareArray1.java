package easy.question6_sorted_square_array;

import java.util.Arrays;

public class SortedSquareArray1 {

    public static void main(String[] args) {
        var input = new int[] {1, 2, 3, 5, 6, 8, 9};
        var expected = new int[] {1, 4, 9, 25, 36, 64, 81};
        var actual = new SortedSquareArray1().sortedSquaredArray(input);
        for (int i = 0; i < expected.length; i++) {
            System.out.println(expected[i] == actual[i]);
        }
    }

    public int[] sortedSquaredArray(int[] array) {
        int[] sortedSquares = new int[array.length];
        for(int idx = 0; idx < array.length; idx++){
            int value = array[idx];
            sortedSquares[idx] = value * value;
        }
        Arrays.sort(sortedSquares);
        return sortedSquares;
    }
}
