public class maxProdTwoPalins {
    // Because this is backtracking, need global var
    int max = 0;
    public static void main(String[] args){
        maxProdTwoPalins s = new maxProdTwoPalins();
        s.maxProduct("KappaKappa");
    }

    public int maxProduct(String s){
        // Make a char array for faster indexing
        char[] c = s.toCharArray();
        // Perform depth-first searching to find max
        dfs(c, 0, "", "");
        return max;
    }

    // Return nothing because this is updating max and that is all that is needed
    public void dfs(char[] c, int i, String s1, String s2){
        // Only begin evaluating palindromes once every combination in c has been created
        if(i >= c.length){
            // Need to check so see if both strings are palindromes
            if(isPalin(s1) && isPalin(s2)){
                // If so, see if max can be updated with the product of their lengths
                max = Math.max(max, s1.length()*s2.length());
                // return, because this path has found a solution
            }
            return;
        }
        // This section makes recursive calls to build up all possible substrings in c
        dfs(c, i+1, s1+c[i], s2);
        dfs(c, i+1, s1, s2+c[i]);
        dfs(c, i+1, s1, s2);
    }

    public boolean isPalin(String s){
        int i = 0;
        int j = s.length() - 1;
        while(i < j){
            // Do the palindrome checking in loop, this statement does verification
            if(s.charAt(i) != s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
