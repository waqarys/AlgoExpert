public class CaesarCipherEncryptor {
    public static String caesarCypherEncryptor(String str, int key) {
        int k = key % 26;
        StringBuilder sb = new StringBuilder();
        for (char c : str.toCharArray()) sb.append((char) ('a' + (c - 'a' + k) % 26));
        return sb.toString();
    }
}
