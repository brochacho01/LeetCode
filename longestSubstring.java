import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
// https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/127839/longest-substring-without-repeating-characters/

public class longestSubstring {

    public static void main(String[] args) {
        String s = "abcabcbb";
        // String s = "abba";
        int result = lengthOfLongestSubstring(s);
        System.out.println(result);
    }

    public static int lengthOfLongestSubstring(String s) {
        if(s.isEmpty()){
            return 0;
        }
        HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
        int strStart = 0;
        int strCont = 1;
        int startIndex = 2;
        int contIndex = 3;
        int len = s.length();
        int[][] dTable = new int[4][len];
        dTable[strStart][0] = 1;
        dTable[strCont][0] = 1;
        dTable[startIndex][0] = 0;
        dTable[contIndex][0] = 0;
        dict.put(s.charAt(0), 0);
        for (int i = 1; i < len; i++) {
            // Two decisions for each char, either substring starts there or continues there
            // If it continues from there, take max from prev + 1
            int isRepeat = 0;
            int repeatIndex = -1;
            char curChar = s.charAt(i);
            // Check to see if this character already exists before it
            for (Character key : dict.keySet()) {
                if (key == curChar) {
                    isRepeat = 1;
                    repeatIndex = dict.get(key);
                    break;
                }
            }
            // Standard Procedure
            if (isRepeat == 0) {
                int prevMax = dTable[strStart][i - 1];
                // If this is a continuation of a substring
                if (dTable[strCont][i - 1] > prevMax) {
                    prevMax = dTable[strCont][i - 1];
                    // Get where substring started
                    dTable[contIndex][i] = dTable[contIndex][i - 1];
                } else {
                    dTable[contIndex][i] = dTable[startIndex][i - 1];
                }
                dTable[strCont][i] = prevMax + 1;
                dTable[startIndex][i] = i;
                dTable[contIndex][i] = dTable[contIndex][i - 1];
                dict.put(curChar, i);
            } else {
                // If character is repeat, check position of predecessor vs. position of
                // beginning of current
                // Update start of cont substring to index just after last occurrence
                // dTable[contIndex][i] = repeatIndex + 1;
                if(repeatIndex < dTable[contIndex][i - 1]){
                    dTable[contIndex][i] = dTable[contIndex][i - 1];
                } else {
                    dTable[contIndex][i] = dTable[startIndex][repeatIndex] + 1;
                }
                int accumulator = 0;
                for(int j = dTable[contIndex][i]; j <= i; j++){
                    accumulator++;
                }
                dTable[strCont][i] = accumulator;
                dict.put(curChar, i);
            }
            dTable[strStart][i] = 1;
            dTable[startIndex][i] = i;
        }
        int max = 1;
        for (int i = 0; i < len; i++) {
            int start = dTable[0][i];
            int cont = dTable[1][i];
            if (start > max) {
                max = start;
            }
            if (cont > max) {
                max = cont;
            }
        }
        return max;
    }
}
