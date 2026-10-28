package easy.searching;

/**
 * Find Three Largest Numbers: return the three largest values (sorted ascending) without sorting the input.
 * Time: O(n) | Space: O(1).
 */
public class FindThreeLargestNumbers {
    public static int[] findThreeLargestNumbers(int[] array) {
        int[] top = {Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE};
        for (int x : array) {
            if (x > top[2]) { top[0] = top[1]; top[1] = top[2]; top[2] = x; }
            else if (x > top[1]) { top[0] = top[1]; top[1] = x; }
            else if (x > top[0]) top[0] = x;
        }
        return top;
    }
}
