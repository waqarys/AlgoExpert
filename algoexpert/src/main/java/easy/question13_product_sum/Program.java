package easy.question13_product_sum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in a "special" array and returns its product sum.
 * </p>
 * <p>
 *   A "special" array is a non-empty array that contains either integers or other
 *   "special" arrays. The product sum of a "special" array is the sum of its
 *   elements, where "special" arrays inside it are summed themselves and then
 *   multiplied by their level of depth.
 * </p>
 * <p>
 *   The depth of a "special" array is how far nested it is. For instance, the
 *   depth of <span>[]</span> is <span>1</span>; the depth of the inner array in
 *   <span>[[]]</span> is <span>2</span>; the depth of the innermost array in
 *   <span>[[[]]]</span> is <span>3</span>.
 * </p>
 * <p>
 *   Therefore, the product sum of <span>[x, y]</span> is <span>x + y</span>; the
 *   product sum of <span>[x, [y, z]]</span> is <span>x + 2 * (y + z)</span>; the
 *   product sum of <span>[x, [y, [z]]]</span> is <span>x + 2 * (y + 3z)</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>12 <span class="CodeEditor-promptComment">// calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)</span>
 * </pre>
 * </div>
 */
public class Program {

    public static void main(String[] args) {
        List<Object> test =
                new ArrayList<Object>(
                        Arrays.asList(
                                5,
                                2,
                                new ArrayList<Object>(Arrays.asList(7, -1)),
                                3,
                                new ArrayList<Object>(
                                        Arrays.asList(6, new ArrayList<Object>(Arrays.asList(-13, 8)), 4))));
        System.out.println(productSum(test) == 12);
    }

    public static int productSum(List<Object> array) {
        return productSumHelper(array, 1);
    }

    public static int productSumHelper(List<Object> array, int multiplier) {
        int sum = 0;
        for (Object el: array) {
            if (el instanceof ArrayList) {
                @SuppressWarnings("unchecked")
                ArrayList<Object> ls = (ArrayList<Object>) el;
                sum += productSumHelper(ls, multiplier + 1);
            } else {
                sum += (int) el;
            }
        }
        return sum * multiplier;
    }
}
