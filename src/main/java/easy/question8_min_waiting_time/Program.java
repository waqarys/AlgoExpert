package easy.question8_min_waiting_time;

import java.util.*;

/**
 * Explanation:
 * 3, 2, 1, 2, 6
 * Sort input
 * 1, 2, 2, 3, 6
 * 4 * 1 = 4
 * 2, 2, 3, 6
 * 3 * 2 = 6
 * 2, 3, 6
 * 2 * 2 = 4
 * 3, 6
 * 1 * 3 = 3
 *
 * Total = 4 + 6 + 4 + 3 = 17
 */
class Program {

    // O|(nlog(n)) | O(1) space
    public int minimumWaitingTime(int[] queries) {
        Arrays.sort(queries);

        int totalWaitingTime = 0;
        for (int idx = 0; idx < queries.length; idx++) {
            int duration = queries[idx];
            int queriesLeft = queries.length - (idx + 1);
            totalWaitingTime += duration * queriesLeft;
        }

        return totalWaitingTime;
    }
}

class ProgramTest {
    public static void main(String[] args) {
        int[] queries = new int[]{3, 2, 1, 2, 6};
        int expected = 17;
        var actual = new Program().minimumWaitingTime(queries);
        System.out.println(expected == actual);
    }
}