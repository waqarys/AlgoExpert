package heap;

import java.util.*;

/**
 * LC 621 Task Scheduler.
 * Approach: greedy formula from the most frequent task (heap simulation included for teaching).
 * Time O(N), Space O(1).
 */
public class TaskScheduler {
    public int leastInterval(char[] tasks, int n) {
        int[] f = new int[26];
        for (char t : tasks) f[t - 'A']++;
        int max = 0, countMax = 0;
        for (int x : f) {
            if (x > max) { max = x; countMax = 1; }
            else if (x == max) countMax++;
        }
        return Math.max(tasks.length, (max - 1) * (n + 1) + countMax);
    }

    /** Simulation: max-heap of remaining counts + cooldown queue of (count, readyTime). */
    public int leastIntervalSim(char[] tasks, int n) {
        int[] f = new int[26];
        for (char t : tasks) f[t - 'A']++;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int x : f) if (x > 0) pq.add(x);
        Deque<int[]> cool = new ArrayDeque<>();
        int time = 0;
        while (!pq.isEmpty() || !cool.isEmpty()) {
            time++;
            if (!pq.isEmpty()) {
                int left = pq.poll() - 1;
                if (left > 0) cool.add(new int[]{left, time + n});
            }
            if (!cool.isEmpty() && cool.peek()[1] == time) pq.add(cool.poll()[0]);
        }
        return time;
    }
}
