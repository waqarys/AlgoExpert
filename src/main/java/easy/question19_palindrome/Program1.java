package easy.question19_palindrome;

public class Program1 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("abcdcba"));
    }

    public static boolean isPalindrome(String str) {
        StringBuilder reversedString = new StringBuilder();
        for (int i = str.length() -1; i >= 0; i--) {
            reversedString.append(str.charAt(i));
        }
        return str.equals(reversedString.toString());
    }
}
