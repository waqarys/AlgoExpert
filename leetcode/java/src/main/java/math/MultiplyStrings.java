package math;

/**
 * LC 43 Multiply Strings.
 * Approach: grade-school multiplication into an int[m+n] with carries.
 * Time O(mn), Space O(m+n).
 */
public class MultiplyStrings {
    public String multiply(String a, String b) {
        int m = a.length(), n = b.length();
        int[] res = new int[m + n];
        for (int i = m - 1; i >= 0; i--)
            for (int j = n - 1; j >= 0; j--) {
                int sum = (a.charAt(i) - '0') * (b.charAt(j) - '0') + res[i + j + 1];
                res[i + j + 1] = sum % 10;
                res[i + j] += sum / 10;
            }
        StringBuilder sb = new StringBuilder();
        for (int d : res) if (!(sb.length() == 0 && d == 0)) sb.append(d);
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
