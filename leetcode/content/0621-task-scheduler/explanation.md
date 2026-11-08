# 0621. Task Scheduler

**Difficulty:** Medium | **Category:** Heap / Priority Queue | **LeetCode:** https://leetcode.com/problems/task-scheduler/

## Problem
- Tasks are letters; identical tasks need at least n intervals between them. Each interval runs one task or idles. Return the minimum total intervals.
- Example: [A,A,A,B,B,B], n = 2 -> 8 (A B idle A B idle A B).

## Intuition
- The most frequent task dictates the skeleton: maxFreq blocks, separated by n slots: (maxFreq - 1) * (n + 1) + (number of tasks with maxFreq).
- If there are enough other tasks to fill every gap, no idling is needed and the answer is just the task count.

## Brute Force
- Simulate with a max-heap of counts and a cooldown queue: O(total * log 26). Correct, and good to show.

## Optimal Approach
1. Count frequencies; maxFreq and countMax = how many letters reach maxFreq.
2. Answer = max(tasks.length, (maxFreq - 1) * (n + 1) + countMax).

## Worked Example
- [A,A,A,B,B,B], n = 2.
```text
maxFreq=3 (A and B) countMax=2
(3-1)*(2+1)+2 = 8 ; tasks=6 ; answer max(6,8)=8
layout: A B _ | A B _ | A B
```

## Complexity
- Time: O(N). Space: O(26).

## Pitfalls
- Forgetting the max with tasks.length when n is small (n = 0 -> answer is N).

## Video Script
- Draw the frame of A's with gaps, then show other tasks filling the gaps.

## Solution
```java file=heap/TaskScheduler.java
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
```

## Tests
```java test=heap/TaskSchedulerTest.java
package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TaskSchedulerTest {
    TaskScheduler s = new TaskScheduler();
    @Test void examples() {
        char[] t = "AAABBB".toCharArray();
        assertEquals(8, s.leastInterval(t, 2));
        assertEquals(6, s.leastInterval(t, 0));
        assertEquals(16, s.leastInterval("AAAAAABCDEFG".toCharArray(), 2));
        assertEquals(8, s.leastIntervalSim(t, 2));
        assertEquals(16, s.leastIntervalSim("AAAAAABCDEFG".toCharArray(), 2));
        assertEquals(6, s.leastIntervalSim(t, 0));
    }
}
```
