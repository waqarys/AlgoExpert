# 0981. Time Based Key-Value Store

**Difficulty:** Medium | **Category:** Binary Search | **LeetCode:** https://leetcode.com/problems/time-based-key-value-store/

## Problem
- set(key, value, timestamp) stores a version; get(key, timestamp) returns the value with the largest timestamp <= the given one, or "".
- Timestamps for set are strictly increasing.

## Intuition
- Because timestamps arrive in increasing order, each key's history list is already sorted.
- get is "rightmost timestamp <= t", a classic upper-bound binary search.
- (A TreeMap.floorEntry also works and is worth mentioning.)

## Brute Force
- Scan the key's history backwards: O(n) per get.

## Optimal Approach
1. Map<String, List<(ts, value)>>.
2. set appends.
3. get: binary search for the last index with ts <= t.

## Worked Example
```text
set(foo, bar, 1)     foo: [(1,bar)]
get(foo, 1) -> bar
get(foo, 3) -> bar   (last ts <= 3 is 1)
set(foo, bar2, 4)    foo: [(1,bar),(4,bar2)]
get(foo, 4) -> bar2
get(foo, 5) -> bar2
get(foo, 0) -> ""
```

## Complexity
- set O(1), get O(log n). Space O(total sets).

## Pitfalls
- Missing key and timestamp before the first version both return "".

## Video Script
- Connect to real systems: MVCC databases and versioned config stores use exactly this lookup.

## Solution
```java file=binarysearch/TimeMap.java
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
```

## Tests
```java test=binarysearch/TimeMapTest.java
package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TimeMapTest {
    @Test void example() {
        TimeMap t = new TimeMap();
        t.set("foo", "bar", 1);
        assertEquals("bar", t.get("foo", 1));
        assertEquals("bar", t.get("foo", 3));
        t.set("foo", "bar2", 4);
        assertEquals("bar2", t.get("foo", 4));
        assertEquals("bar2", t.get("foo", 5));
        assertEquals("", t.get("foo", 0));
        assertEquals("", t.get("nope", 9));
    }
}
```
