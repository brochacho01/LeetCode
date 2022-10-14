public class atoi {
    public int myAtoi(String s) {
        // first need to read in leading 0's
        int strLen = s.length();
        int lenNums = 0;
        int sign = 1;
        // Count the num of leading 0's
        // Also check for negative flag
        int i = 0;
        int numStart = -1;
        int numEnd = -1;
        while(true){
            // First read in whitespace
            while(s.charAt(i) == ' '){
                i++;
            }
            if(s.charAt(i) == '-'){
                sign = -1;
            }
            i++;
            // Then read in int count;
            numStart = i;
            while((i < strLen) && Character.isDigit(s.charAt(i))){
                lenNums++;
            }
            numEnd = i;
        }
        // At this point we know where the number lies in the string, and how many number chars there are, need to convert that section of string to int
        

    }
}
