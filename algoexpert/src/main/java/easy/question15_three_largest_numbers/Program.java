package easy.question15_three_largest_numbers;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an array of at least three integers and,
 *   without sorting the input array, returns a sorted array of the three largest
 *   integers in the input array.
 * </p>
 * <p>
 *   The function should return duplicate integers if necessary; for example, it
 *   should return <span>[10, 10, 12]</span> for an input array of
 *   <span>[10, 5, 9, 10, 12]</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[18, 141, 541]
 * </pre>
 * </div>
 */
public class Program {
    public static void main(String[] args) {
        int[] threeLargest = findThreeLargestNumbers(new int[] {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7});
        for(int num: threeLargest) System.out.println(num);
    }

    public static int[] findThreeLargestNumbers(int[] array) {
        int[] threeLargest = {Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE};
        for (int num : array) {
            updateLargest(threeLargest, num);
        }
        return threeLargest;
    }

    public static void updateLargest(int[] threeLargest, int num) {
        if (num > threeLargest[2]) {
            shiftAndUpdate(threeLargest, num, 2);
        } else if (num > threeLargest[1]) {
            shiftAndUpdate(threeLargest, num, 1);
        } else if (num > threeLargest[0]) {
            shiftAndUpdate(threeLargest, num, 0);
        }
    }

    public static void shiftAndUpdate(int[] array, int num, int idx) {
        for (int i = 0; i <= idx; i++) {
            if (i == idx) {
                array[i] = num;
            } else {
                array[i] = array[i + 1];
            }
        }
    }
}
