package leetcode;

public class LongestCommonPrefix {
    public static void main(String[] args){
        String[] strs = {""};
        System.out.println(lCP(strs));
    }


    public static String lCP(String[] strs){
        String result = "";
        int arlen = strs.length;
        int difference = 0;
        int curCommon = 0;
        while(difference == 0){
            if(strs[0].length() <= curCommon){
                break;
            }
            char curChar = strs[0].charAt(curCommon);
            for(int i = 1; i < arlen; i++){
                if(strs[i].length() <= curCommon){
                    difference = 1;
                    break;
                }
                if(strs[i].charAt(curCommon) != curChar){
                    difference = 1;
                    break;
                }
            }
            if(difference == 0){
                result = result + curChar;
                curCommon++;
            }
        }
        return result;
    }
}
