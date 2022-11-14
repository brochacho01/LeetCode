import java.util.Arrays;
import java.util.List;

public class wordBreak {
    public static void main(String[] args){
        // String s = "applepenapple";
        // List<String> wordDict = Arrays.asList("apple", "pen");
        String s = "catsandogs";
        List<String> wordDict = Arrays.asList("cats", "sand", "dogs", "cat", "dog");
        System.out.println(wordbreak(s, wordDict));
    }
    public static boolean wordbreak(String s, List<String> wordDict){
        //length + 1 because substring() has end index as exclusive so we need to go one more than s.length, therefore we need to extend everything by one
        boolean[] res = new boolean[s.length() + 1];
        res[0] = true;
        for(int i = 1; i <= s.length(); i++){
            for(int j = 0; j < i; j++){
                // the if res[j] is very important, because if the res array does not have a true there, that means that certain characters are being excluded
                if(res[j] && wordDict.contains(s.substring(j, i))){
                    res[i] = true;
                    break;
                }
            }
        }
        return res[s.length()];
    }
}
