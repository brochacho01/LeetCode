public class atoi {
    public static void main(String[] args) {
        int i = myAtoi("-91283472332");
        System.out.println(i);
    }

    public static int myAtoi(String s) {
        // first need to read in leading 0's
        int strLen = s.length();
        int lenNums = 0;
        int sign = 1;
        // Count the num of leading 0's
        // Also check for negative flag
        int i = 0;
        int numStart = -1;
        int numEnd = -1;
        // First read in whitespace
        while (s.charAt(i) == ' ') {
            i++;
        }
        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        }
        if(s.charAt(i) == '+') {
            i++;
        }
        // Then read in int count;
        numStart = i;
        while ((i < strLen) && Character.isDigit(s.charAt(i))) {
            lenNums++;
            i++;
        }
        numEnd = i;
        // At this point we know where the number lies in the string, and how many
        // number chars there are, need to convert that section of string to int
        int[] arr = new int[lenNums];
        int j = 0;
        for(i = numStart; i < numEnd; i++){
            arr[j] = (int) s.charAt(i) - '0';
            j++;
        }
        // Now convert to int
        int result = 0;
        int power = 1;
        for(i = lenNums - 1; i>= 0; i--){
            result += (arr[i] * power);
            power *= 10;
        }
        result *= sign;
        if(result > (Math.pow(2, 31)) - 1){
            result = (int)(Math.pow(2, 31)) - 1;
        } else if(result < Math.pow(-2, 31)){
            result = (int)(Math.pow(-2, 31));
        }
        return result;
    }
}
