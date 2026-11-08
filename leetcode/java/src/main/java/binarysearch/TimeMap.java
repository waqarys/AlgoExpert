package binarysearch;

import java.util.*;

/**
 * LC 981 Time Based Key-Value Store.
 * Approach: per-key append-only list (sorted by ts); get = binary search for last ts <= t.
 * set O(1), get O(log n).
 */
public class TimeMap {
    private record Entry(int ts, String value) {}
    private final Map<String, List<Entry>> store = new HashMap<>();

    public void set(String key, String value, int timestamp) {
        store.computeIfAbsent(key, k -> new ArrayList<>()).add(new Entry(timestamp, value));
    }

    public String get(String key, int timestamp) {
        List<Entry> list = store.get(key);
        if (list == null) return "";
        int lo = 0, hi = list.size() - 1, ans = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (list.get(mid).ts() <= timestamp) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans == -1 ? "" : list.get(ans).value();
    }
}
