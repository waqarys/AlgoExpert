package medium.greedyalgorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

/**
 * <div class="html">
 * <p>
 *   You're given an integer <span>k</span> representing a number of workers and an
 *   array of positive integers representing durations of tasks that must be
 *   completed by the workers. Specifically, each worker must complete two unique
 *   tasks and can only work on one task at a time. The number of tasks will always
 *   be equal to <span>2k</span> such that each worker always has exactly two tasks
 *   to complete. All tasks are independent of one another and can be completed in
 *   any order. Workers will complete their assigned tasks in parallel, and the
 *   time taken to complete all tasks will be equal to the time taken to complete
 *   the longest pair of tasks (see the sample output for an explanation).
 * </p>
 * <p>
 *   Write a function that returns the optimal assignment of tasks to each worker
 *   such that the tasks are completed as fast as possible. Your function should
 *   return a list of pairs, where each pair stores the indices of the tasks that
 *   should be completed by one worker. The pairs should be in the following
 *   format: <span>[task1, task2]</span>, where the order of <span>task1</span> and
 *   <span>task2</span> doesn't matter. Your function can return the pairs in any
 *   order. If multiple optimal assignments exist, any correct answer will be
 *   accepted.
 * </p>
 * <p>
 *   Note: you'll always be given at least one worker (i.e., <span>k</span> will
 *   always be greater than <b>0</b>).
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">k</span> = 3
 * <span class="CodeEditor-promptParameter">tasks</span> = [1, 3, 5, 3, 1, 4]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[
 *   [0, 2], <span class="CodeEditor-promptComment">// tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6</span>
 *   [4, 5], <span class="CodeEditor-promptComment">// tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5</span>
 *   [1, 3], <span class="CodeEditor-promptComment">// tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6</span>
 * ] <span class="CodeEditor-promptComment">// The fastest time to complete all tasks is 6.</span>
 *
 * <span class="CodeEditor-promptComment">// Note: there are multiple correct answers for this sample input.</span>
 * <span class="CodeEditor-promptComment">// The following is an example of another correct answer:</span>
 * <span class="CodeEditor-promptComment">// [</span>
 * <span class="CodeEditor-promptComment">//   [2, 4],</span>
 * <span class="CodeEditor-promptComment">//   [0, 5],</span>
 * <span class="CodeEditor-promptComment">//   [1, 3]</span>
 * <span class="CodeEditor-promptComment">// [</span>
 * </pre>
 * </div>
 */
public class TaskAssignment {
    public static void main(String[] args) {
        var k = 3;
        var tasks = new ArrayList<Integer>(Arrays.asList(1, 3, 5, 3, 1, 4));
        var expected = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> subarr = new ArrayList<Integer>(Arrays.asList(4, 2));
        ArrayList<Integer> subarr2 = new ArrayList<Integer>(Arrays.asList(0, 5));
        ArrayList<Integer> subarr3 = new ArrayList<Integer>(Arrays.asList(3, 1));
        expected.add(subarr);
        expected.add(subarr2);
        expected.add(subarr3);
        var actual = new TaskAssignment().taskAssignment(k, tasks);
        System.out.println(expected.equals(actual));
    }

    // O(nlog(n)) time | O(n) space - n is the number of tasks
    public ArrayList<ArrayList<Integer>> taskAssignment(int k, ArrayList<Integer> tasks) {
        ArrayList<ArrayList<Integer>> pairedTasks = new ArrayList<ArrayList<Integer>>();
        HashMap<Integer, ArrayList<Integer>> taskDurationsToIndices = getTaskDurationsToIndices(tasks);

        ArrayList<Integer> sortedTasks = tasks;
        Collections.sort(sortedTasks);

        for (int idx = 0; idx < k; idx++) {
            int task1Duration = sortedTasks.get(idx);
            ArrayList<Integer> indicesWithTask1Duration = taskDurationsToIndices.get(task1Duration);
            int task1Index = indicesWithTask1Duration.remove(indicesWithTask1Duration.size() - 1);

            int task2SortedIndex = tasks.size() - 1 - idx;
            int task2Duration = sortedTasks.get(task2SortedIndex);
            ArrayList<Integer> indicesWithTask2Duration = taskDurationsToIndices.get(task2Duration);
            int task2Index = indicesWithTask2Duration.remove(indicesWithTask2Duration.size() - 1);

            ArrayList<Integer> pairedTask = new ArrayList<Integer>();
            pairedTask.add(task1Index);
            pairedTask.add(task2Index);
            pairedTasks.add(pairedTask);
        }

        return pairedTasks;
    }

    public HashMap<Integer, ArrayList<Integer>> getTaskDurationsToIndices(ArrayList<Integer> tasks) {
        HashMap<Integer, ArrayList<Integer>> taskDurationsToIndices =
                new HashMap<Integer, ArrayList<Integer>>();

        for (int idx = 0; idx < tasks.size(); idx++) {
            int taskDuration = tasks.get(idx);
            if (taskDurationsToIndices.containsKey(taskDuration)) {
                taskDurationsToIndices.get(taskDuration).add(idx);
            } else {
                ArrayList<Integer> temp = new ArrayList<Integer>();
                temp.add(idx);
                taskDurationsToIndices.put(taskDuration, temp);
            }
        }

        return taskDurationsToIndices;
    }
}
