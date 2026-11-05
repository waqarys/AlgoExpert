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
