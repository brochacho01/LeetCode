package leetcode;
public class RomantoInteger {
    // https://leetcode.com/problems/roman-to-integer/
    public static void main(String[] args) {
        String S = "III";
        RomantoInteger R = new RomantoInteger();
        int result = R.rToInt(S);
        System.out.println(result);
    }

    public static int rToInt(String s) {
        int i = s.length();
        int j = 0;
        int result = 0;
        while (j < i) {
            if (s.charAt(j) == 'I') {
                if (j + 1 < i) {
                    if (s.charAt(j + 1) == 'V') {
                        result += 4;
                        j += 2;
                    } else if (s.charAt(j + 1) == 'X') {
                        result += 9;
                        j += 2;
                    } else {
                        result += 1;
                        j++;
                    }
                } else {
                    result += 1;
                    j++;
                }
            } else if (s.charAt(j) == 'V') {
                result += 5;
                j++;
            } else if (s.charAt(j) == 'X') {
                if (j + 1 < i) {
                    if (s.charAt(j + 1) == 'L') {
                        result += 40;
                        j += 2;
                    } else if (s.charAt(j + 1) == 'C') {
                        result += 90;
                        j += 2;
                    } else {
                        result += 10;
                        j++;
                    }
                } else {
                    result += 10;
                    j++;
                }
            } else if (s.charAt(j) == 'L') {
                result += 50;
                j++;
            } else if (s.charAt(j) == 'C') {
                if (j + 1 < i) {
                    if (s.charAt(j + 1) == 'D') {
                        result += 400;
                        j += 2;
                    } else if (s.charAt(j + 1) == 'M') {
                        result += 900;
                        j += 2;
                    } else {
                        result += 100;
                        j++;
                    }
                } else {
                    result += 100;
                    j++;
                }
            } else if (s.charAt(j) == 'D') {
                result += 500;
                j++;
            } else if (s.charAt(j) == 'M') {
                result += 1000;
                j++;
            }
        }
        return result;
    }
}