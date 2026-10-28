public class LongestMostFrequentPrefix {
    private static class Node { final Map<Character, Node> next = new HashMap<>(); int count; }

    public static String longestMostFrequentPrefix(String[] strings) {
        Node root = new Node();
        int bestCount = 0;
        String best = "";
        for (String s : strings) {
            Node n = root;
            for (int i = 0; i < s.length(); i++) {
                n = n.next.computeIfAbsent(s.charAt(i), k -> new Node());
                n.count++;
            }
        }
        for (String s : strings) {
            Node n = root;
            for (int i = 0; i < s.length(); i++) {
                n = n.next.get(s.charAt(i));
                if (n.count > bestCount || (n.count == bestCount && i + 1 > best.length())) {
                    bestCount = n.count;
                    best = s.substring(0, i + 1);
                }
            }
        }
        return best;
    }
