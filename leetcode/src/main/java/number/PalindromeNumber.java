package number;

public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        if(x < 0) return false;

        String str = Integer.toString(x);
        for(int i = 0; i < str.length()/2; i++) {
            if(str.charAt(i) != str.charAt(str.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public boolean isPalindrome1(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;

        int num = x;
        int y = 0;

        while(num != 0) {
            int rem = num % 10;
            num = num / 10;
            y = y * 10 + rem;
        }

        return y == x;
    }
}
