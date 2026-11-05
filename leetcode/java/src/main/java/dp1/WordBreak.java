package dp1;

import java.util.*;

/**
 * LC 139 Word Break.
 * Approach: dp[i] = some j with dp[j] && s[j..i) in dict; j limited by the longest word.
 * Time O(n * L^2), Space O(n).
 */
public class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        int maxLen = 0;
        for (String w : wordDict) maxLen = Math.max(maxLen, w.length());
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++)
            for (int j = i - 1; j >= Math.max(0, i - maxLen); j--)
                if (dp[j] && dict.contains(s.substring(j, i))) { dp[i] = true; break; }
        return dp[s.length()];
    }
}
