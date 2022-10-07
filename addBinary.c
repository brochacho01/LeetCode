#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// https://leetcode.com/problems/add-binary/description/
char *addBinary(char *a, char*b);

int main(){
    char *a = "111";
    char *b = "111";
    char *result = addBinary(a,b);
    printf("Test\n");
}

char *addBinary(char *a, char *b)
{
    int aBin[32];
    int bBin[32];
    int result[32];
    int i;
    int aLen = strlen(a);
    int bLen = strlen(b);
    for(i = 0; i < 32; i++){
        aBin[i] = -1;
        bBin[i] = -1;
        result[i] = -1;
    }
    int aInt = atoi(a);
    int bInt = atoi(b);
    // Convert a to binary
    i = 0;
    while(aInt > 0){
        aBin[i]= aInt % 2;
        aInt /= 10;
        i++;
    }
    i = 0;
    while(bInt > 0){
        bBin[i]= bInt % 2;
        bInt /= 10;
        i++;
    }
    int addResult;
    int remainder = 0;
    // Do binary add
    i = 0;
    while ((aBin[i] != -1) && (bBin[i] != -1))
    {
        addResult = aBin[i] + bBin[i] + remainder;
        if (addResult == 2)
        {
            addResult = 0;
            remainder = 1;
        }
        else if (addResult == 3)
        {
            addResult = 1;
            remainder = 1;
        }
        result[i] = addResult;
        i++;
    }
    if (aBin[i] != -1)
    {
        while (aBin[i] != -1)
        {
            addResult = aBin[i] + remainder;
            if (addResult == 2)
            {
                addResult = 0;
                remainder = 1;
            }
            result[i] = addResult;
            i++;
        }
    }
    if (bBin[i] != -1)
    {
        while (bBin[i] != -1)
        {
            addResult = bBin[i] + remainder;
            if (addResult == 2)
            {
                addResult = 0;
                remainder = 1;
            }
            result[i] = addResult;
            i++;
        }
    }
    if(remainder == 1){
        result[i] = remainder;
    }
    // Need to convert result into string
    int numchars = i+1;
    char *ret;
    ret = (char*)malloc(sizeof(char) * numchars);
    while(i > 0){
    	if(result[i] == 1){
            ret[i] = '1';
        } else {
            ret[i] = '0';
        }
        i--;
    }
    return ret;
}
