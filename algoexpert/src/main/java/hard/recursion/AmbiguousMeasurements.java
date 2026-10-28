package hard.recursion;

import java.util.HashMap;
import java.util.Map;

/**
 * Ambiguous Measurements: measuring cups each measure a [low, high] range. Can repeated pours produce a
 * volume within [low, high]? Memoised search over remaining (low, high) targets.
 * Time: O(low * high * n) | Space: O(low * high).
 */
public class AmbiguousMeasurements {
    public static boolean ambiguousMeasurements(int[][] cups, int low, int high) {
        return can(cups, low, high, new HashMap<>());
    }

    private static boolean can(int[][] cups, int low, int high, Map<String, Boolean> memo) {
        String key = low + ":" + high;
        if (memo.containsKey(key)) return memo.get(key);
        if (low <= 0 && high <= 0) return false;
        boolean ok = false;
        for (int[] c : cups) {
            if (c[1] == 0) continue; // an empty cup never makes progress (avoids infinite recursion)
            if (c[0] >= low && c[1] <= high) { ok = true; break; }
            if (can(cups, Math.max(0, low - c[0]), Math.max(0, high - c[1]), memo)) { ok = true; break; }
        }
        memo.put(key, ok);
        return ok;
    }
}
