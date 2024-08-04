import java.util.Arrays;
import java.util.Comparator;

public class MinimumSwapsDescending {
    public static int minimumSwaps(int[] arr) {
        int n = arr.length;
        boolean[] visited = new boolean[n];
        int swaps = 0;

        // Create an array of pairs where each pair is (element, index)
        Pair[] arrPos = new Pair[n];
        for (int i = 0; i < n; i++) {
            arrPos[i] = new Pair(arr[i], i);
        }

        // Sort the array by element values in descending order
        Arrays.sort(arrPos, (pair1, pair2) -> Integer.compare(pair2.value, pair1.value));

        // Traverse the array and count cycles
        for (int i = 0; i < n; i++) {
            // If already visited or already in the correct position
            if (visited[i] || arrPos[i].index == i) {
                continue;
            }

            // Find the cycle size
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = arrPos[j].index;
                cycleSize++;
            }

            // Add the number of swaps for this cycle
            if (cycleSize > 0) {
                swaps += (cycleSize - 1);
            }
        }

        return swaps;
    }

    static class Pair {
        int value, index;

        Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

    public static void main(String[] args) {
        int[] arr = {4, 3, 1, 2};
        System.out.println("Minimum swaps required: " + minimumSwaps(arr));
    }
}
