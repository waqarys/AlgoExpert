# 0210. Course Schedule II

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/course-schedule-ii/

## Problem
- Return any valid order to take all courses, or [] if impossible.

## Intuition
- The order in which Kahn's algorithm removes zero in-degree nodes is a topological order.

## Brute Force
- Try permutations and validate: O(n!).

## Optimal Approach
1. Same as problem 207, but append each popped course to the output.
2. If output length < numCourses, return [].

## Worked Example
- n = 4, [[1,0],[2,0],[3,1],[3,2]].
```text
queue [0]       order [0]       indeg 1:0 2:0 -> queue [1,2]
pop 1           order [0,1]     indeg 3:1
pop 2           order [0,1,2]   indeg 3:0 -> queue [3]
pop 3           order [0,1,2,3]
```

## Complexity
- Time: O(V + E). Space: O(V + E).

## Pitfalls
- Several valid orders exist; tests should validate the order rather than compare to one answer.

## Video Script
- Real-world tie-in: build systems and package managers order dependencies this way.

## Solution
```java file=graphs/CourseScheduleII.java
package graphs;

import java.util.*;

/**
 * LC 210 Course Schedule II.
 * Approach: Kahn's algorithm, recording the pop order.
 * Time O(V+E), Space O(V+E).
 */
public class CourseScheduleII {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] indeg = new int[numCourses];
        for (int[] p : prerequisites) { adj.get(p[1]).add(p[0]); indeg[p[0]]++; }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) if (indeg[i] == 0) q.add(i);
        int[] order = new int[numCourses];
        int k = 0;
        while (!q.isEmpty()) {
            int c = q.poll();
            order[k++] = c;
            for (int nx : adj.get(c)) if (--indeg[nx] == 0) q.add(nx);
        }
        return k == numCourses ? order : new int[0];
    }
}
```

## Tests
```java test=graphs/CourseScheduleIITest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CourseScheduleIITest {
    static boolean valid(int n, int[][] pre, int[] order) {
        if (order.length != n) return false;
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) pos[order[i]] = i;
        for (int[] p : pre) if (pos[p[1]] > pos[p[0]]) return false;
        return true;
    }
    CourseScheduleII s = new CourseScheduleII();
    @Test void examples() {
        int[][] pre = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        assertTrue(valid(4, pre, s.findOrder(4, pre)));
        assertArrayEquals(new int[]{0}, s.findOrder(1, new int[][]{}));
        assertArrayEquals(new int[0], s.findOrder(2, new int[][]{{0, 1}, {1, 0}}));
    }
}
```
