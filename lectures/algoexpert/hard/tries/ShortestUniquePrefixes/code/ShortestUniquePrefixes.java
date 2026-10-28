public class ShortestUniquePrefixes {
    private static class Node { final Map<Character, Node> next = new HashMap<>(); int count; }

    public static String[] shortestUniquePrefixes(String[] strings) {
        Node root = new Node();
        for (String s : strings) {
            Node n = root;
            for (char c : s.toCharArray()) { n = n.next.computeIfAbsent(c, k -> new Node()); n.count++; }
        }
        String[] out = new String[strings.length];
        for (int k = 0; k < strings.length; k++) {
            String s = strings[k];
            Node n = root;
            int len = s.length();
            for (int i = 0; i < s.length(); i++) {
                n = n.next.get(s.charAt(i));
                if (n.count == 1) { len = i + 1; break; }
            }
            out[k] = s.substring(0, len);
        }
        return out;
    }
