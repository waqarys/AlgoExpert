package greedy;

/**
 * LC 1899 Merge Triplets to Form Target Triplet.
 * Approach: discard triplets exceeding target anywhere; check each coordinate is hit exactly.
 * Time O(n), Space O(1).
 */
public class MergeTripletsToFormTarget {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        boolean[] found = new boolean[3];
        for (int[] t : triplets) {
            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]) continue;
            for (int k = 0; k < 3; k++) if (t[k] == target[k]) found[k] = true;
        }
        return found[0] && found[1] && found[2];
    }
}
