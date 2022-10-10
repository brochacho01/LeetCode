public class BreakPalindrome {
    public static void main(String[] args){
        String palindrome = "aa";
        System.out.println(breakPalindrome(palindrome));
    }
    public static String breakPalindrome(String palindrome) {
        // First break string in two
        int strLen = palindrome.length();
        if (strLen <= 1) {
            return "";
        }
        char[] palin = palindrome.toCharArray();
        int j = 0;
        int minChar = 'a';
        int isSwap = 0;
        // Check to see if the midpoint falls on a character
        if (strLen / 2 == 1) {
            while(isSwap == 0){
                if(palin[1] != ((char)(minChar + j))){
                    palin[1] = ((char)(minChar + j));
                    isSwap = 1;
                }
                j++;
            }
            String result = new String(palin);
            return result;
        }
        // Scan string to see first letter that can be replaced with a
        // if all a's find first one that can be replaced with b
        while (true) {
            for (int i = 0; i < strLen / 2; i++) {
                if (palin[i] != ((char)(minChar + j))) {
                    palin[i] = ((char)(minChar + j));
                    isSwap = 1;                        
                    break;
                }
            }
            if(isSwap == 1){
                break;
            }
            j++;
        }
        String result = new String(palin);
        return result;
    }
}
