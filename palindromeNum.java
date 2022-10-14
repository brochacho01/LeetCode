public class palindromeNum {
    public static void main(String[] args){
        System.out.println(isPalindrome(1001));
    }

    public static boolean isPalindrome(int x) {
        int count = 0;
        int tempx = x;
        while(tempx != 0) {
            tempx /= 10;
            count++;
        }
        if(x < 0){
            count++;
        }
        int[] xIterable = new int[count];
        int i = count - 1;
        while(x != 0){
            // Negative but not on last val
            if((x < 0) && (x / 10 != 0)){
            xIterable[i] = (x % 10) * -1;
            x/= 10;
            i--;
            // On last val and negative
            } else if(x < 0){
                xIterable[i] = x % 10;
                x/= 10;
                i--;
                xIterable[i] = Integer.MIN_VALUE;
            } else {
                // Standard case
                xIterable[i] = x % 10;
                x/= 10;
                i--;
            }
        }
        int j = count - 1;
        for(i = 0; i < count / 2; i++) {
            if(xIterable[i] != xIterable[j]) {
                return false;
            }
            j--;
        }
        return true;
    }
}
