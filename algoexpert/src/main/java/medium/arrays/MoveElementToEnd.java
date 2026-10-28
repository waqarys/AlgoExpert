package medium.arrays;

import java.util.Collections;
import java.util.List;

/**
 * Move Element To End: in place, move every occurrence of `toMove` to the end (other order irrelevant).
 * Time: O(n) | Space: O(1).
 */
public class MoveElementToEnd {
    public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {
        int l = 0, r = array.size() - 1;
        while (l < r) {
            while (l < r && array.get(r) == toMove) r--;
            if (array.get(l) == toMove) Collections.swap(array, l, r);
            l++;
        }
        return array;
    }
}
