import java.util.Arrays;

public class diagSort {
    public int[][] diagonalSort(int[][] mat) {
        for(int m = 0; m < mat.length; m++) {
            // Want to count num cells in each slice
            int n = 0;
            int count = 0;
            int tempm = m;
            while((n < mat[0].length) && (tempm < mat.length)) {
                count++;
                n++;
                tempm++;
            }
            int[] temparr = new int[count];
            // copy elements into temparr to sort
            n = 0;
            tempm = m;
            int index = 0;
            while(index < count){
                temparr[index] = mat[tempm][n];
                index++;
                n++;
                tempm++;
            }
            Arrays.sort(temparr);
            // Place elements back into mat
            n = 0;
            tempm = m;
            index = 0;
            while(index < count) {
                mat[tempm][n] = temparr[index];
                index++;
                n++;
                tempm++;
            }
        }
        for(int n = 1; n < mat[0].length; n++) {
            int m = 0;
            int count = 0;
            int tempn = n;
            while((m < mat.length) && (tempn < mat[0].length)){
                count++;
                m++;
                tempn++;
            }
            int[] temparr = new int[count];
            m = 0;
            tempn = n;
            int index = 0;
            while(index < count) {
                temparr[index] = mat[m][tempn];
                index++;
                m++;
                tempn++;
            }
            Arrays.sort(temparr);
            m = 0;
            tempn = n;
            index = 0;
            while(index < count) {
                mat[m][tempn] = temparr[index];
                index++;
                m++;
                tempn++;
            }
        }
        return mat;
    }
}
