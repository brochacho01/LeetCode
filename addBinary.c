#include <stdin.h>

char *addBinary(char *a, char *b)
{
    // Create two int arrays
    // Iterate over each char * putting the value of converted binary into respective place in the array
    // do a + on the numbers
    // convert to char *
    // return
    int aBin[32];
    int bBin[32];
    int result[32];
    int aInt = atoi(a);
    int bInt = atoi(b);

    // Convert a to binary
    int i = 0;
    while (aInt > 0)
    {
        aBin[i] = aInt % 2;
        aInt /= 2;
        i++;
    }
    i = 0;
    // Convert b to binary
    while (bInt > 0)
    {
        bBin[i] = bInt % 2;
        bInt /= 2;
        i++;
    }
    int i = 0;
    int addResult;
    int remainder = 0;
    // Do binary add
    while ((aBin[i] != NULL) && (bBin[i] != NULL))
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
    if (aBin[i] != NULL)
    {
        while (aBin[i] != NULL)
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
    if (bBin[i] != NULL)
    {
        while (bBin[i] != NULL)
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
}
