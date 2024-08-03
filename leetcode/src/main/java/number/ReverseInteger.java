package number;

public class ReverseInteger {
    public int reverse(int x) {
        int sign = x < 0 ? -1 : 1;

        int abs = Math.abs(x);
        long rev = 0;
        while(abs > 0) {
            int rem = abs % 10;
            abs = abs / 10;
            rev = rev * 10 + rem;
        }
        if(rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE) return 0;
        return (int) (sign * rev);
    }

    public int reverse1(int x) {
        int sign = x < 0 ? -1 : 1;

        int abs = Math.abs(x);
        int rev = 0;
        while(abs != 0) {
            int rem = abs % 10;
            abs = abs / 10;
            rev = rev * 10 + rem;
        }
        return sign * rev;
    }
}
