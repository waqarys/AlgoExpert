package medium.recursion;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Permutations: all orderings of a list of distinct ints (empty input yields an empty list).
 * Time: O(n * n!) | Space: O(n * n!).
 */
public class Permutations {
    public static List<List<Integer>> getPermutations(List<Integer> array) {
        List<List<Integer>> out = new ArrayList<>();
        if (!array.isEmpty()) permute(0, new ArrayList<>(array), out);
        return out;
    }

    private static void permute(int i, List<Integer> a, List<List<Integer>> out) {
        if (i == a.size() - 1) { out.add(new ArrayList<>(a)); return; }
        for (int j = i; j < a.size(); j++) { Collections.swap(a, i, j); permute(i + 1, a, out); Collections.swap(a, i, j); }
    }
}
