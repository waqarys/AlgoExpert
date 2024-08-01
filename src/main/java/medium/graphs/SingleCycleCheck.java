package medium.graphs;

/**
 * <div class="html">
 * <p>
 *   You're given an array of integers where each integer represents a jump of its
 *   value in the array. For instance, the integer <span>2</span> represents a jump
 *   of two indices forward in the array; the integer <span>-3</span> represents a
 *   jump of three indices backward in the array.
 * </p>
 * <p>
 *   If a jump spills past the array's bounds, it wraps over to the other side. For
 *   instance, a jump of <span>-1</span> at index <span>0</span> brings us to the last index in
 *   the array. Similarly, a jump of <span>1</span> at the last index in the array brings us to
 *   index <span>0</span>.
 * </p>
 * <p>
 *   Write a function that returns a boolean representing whether the jumps in the
 *   array form a single cycle. A single cycle occurs if, starting at any index in
 *   the array and following the jumps, every element in the array is visited
 *   exactly once before landing back on the starting index.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [2, 3, 1, -4, -4, 2]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>true
 * </pre>
 * </div>
 */
public class SingleCycleCheck {
    public static void main(String[] args) {
        System.out.println(hasSingleCycle(new int[] {2, 3, 1, -4, -4, 2}));
    }

    // O(n) time | O(1) space - n is the length of input array
    public static boolean hasSingleCycle(int[] array) {
        int numElementsVisited = 0;
        int currentIdx = 0;
        while (numElementsVisited < array.length) {
            if (numElementsVisited > 0 && currentIdx == 0) return false;
            numElementsVisited++;
            currentIdx = getNextIdx(currentIdx, array);
        }
        return currentIdx == 0;
    }

    public static int getNextIdx(int currentIdx, int[] array) {
        int jump = array[currentIdx];
        int nextIdx = (currentIdx + jump) % array.length;
        return nextIdx >= 0 ? nextIdx : nextIdx + array.length;
    }
}
