public class SmallestSubstringContaining {
    public static String smallestSubstringContaining(String big, String small) {
        Map<Character, Integer> need = new HashMap<>();
        for (char c : small.toCharArray()) need.merge(c, 1, Integer::sum);
        int missing = small.length(), l = 0, bs = 0, be = Integer.MAX_VALUE;
        for (int r = 0; r < big.length(); r++) {
            char c = big.charAt(r);
            if (need.containsKey(c)) { if (need.get(c) > 0) missing--; need.merge(c, -1, Integer::sum); }
            while (missing == 0) {
                if (r - l < be - bs) { bs = l; be = r; }
                char d = big.charAt(l++);
                if (need.containsKey(d)) { need.merge(d, 1, Integer::sum); if (need.get(d) > 0) missing++; }
            }
        }
        return be == Integer.MAX_VALUE ? "" : big.substring(bs, be + 1);
    }
}
