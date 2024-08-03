package string;

public class PalindromeString {
    public boolean isPalindrome(String s) {
        String newString = "";
        for(char c: s.toCharArray()) {
            if(Character.isAlphabetic(c) || Character.isDigit(c)) {
                newString += c;
            }
        }

        newString = newString.toLowerCase();
        int start = 0;
        int end = newString.length() - 1;
        while (start < end) {
            if(newString.charAt(start) != newString.charAt(end)) {
                return false;
            }
            start ++;
            end --;
        }
        return true;
    }
}
