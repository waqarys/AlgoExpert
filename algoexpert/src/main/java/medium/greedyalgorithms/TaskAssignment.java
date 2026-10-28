package medium.greedyalgorithms;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Task Assignment: 2k tasks with durations, k workers doing two tasks each in parallel; minimise the
 * longest worker time. Pair shortest with longest. Returns index pairs.
 * Time: O(n log n) | Space: O(n).
 */
public class TaskAssignment {
    public static List<List<Integer>> taskAssignment(int k, List<Integer> tasks) {
        List<Integer> idx = new ArrayList<>();
        for (int i = 0; i < tasks.size(); i++) idx.add(i);
        idx.sort(Comparator.comparingInt(tasks::get));
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < k; i++) out.add(List.of(idx.get(i), idx.get(idx.size() - 1 - i)));
        return out;
    }
}
