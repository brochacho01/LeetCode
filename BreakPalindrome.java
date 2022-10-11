public class BreakPalindrome {
    // https://leetcode.com/problems/break-a-palindrome/
    public static void main(String[] args) {
        String palindrome = "aba";
        System.out.println(breakPalindrome(palindrome));
    }

    public static String breakPalindrome(String palindrome) {
        // Put string into array
        int strLen = palindrome.length();
        if (strLen <= 1) {
            return "";
        }
        char[] palin = palindrome.toCharArray();
        int mid = -1;
        int isSwap = 0;
        if (strLen % 2 != 0) {
            mid = strLen / 2;
        }
        if (palin[0] != 'a') {
            palin[0] = 'a';
            isSwap = 1;
        }
        // Iterate over first half of string
        if (isSwap == 0) {
            for (int i = 1; i < strLen / 2; i++) {
                if ((palin[i] != 'a') && (i != mid)) {
                    palin[i] = 'a';
                    isSwap = 1;
                }
                if (isSwap == 1) {
                    break;
                }
            }
        }
        if (isSwap == 0) {
            for (int i = strLen / 2; i < strLen - 1; i++) {
                if ((palin[i] != 'a') && (i != mid)) {
                    palin[i] = 'a';
                    isSwap = 1;
                }
                if (isSwap == 1) {
                    break;
                }
            }
        }
        if (isSwap == 0) {
            for (int i = strLen - 1; i > 0; i--) {
                if (palin[i] == 'a') {
                    palin[i] = 'b';
                    isSwap = 1;
                }
                if (isSwap == 1) {
                    break;
                }
            }
        }
        String result = new String(palin);
        return result;
    }
}
