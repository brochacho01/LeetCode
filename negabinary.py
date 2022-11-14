from ast import List

#Better way to do this is to continually pop items off of the arrays, I think there's also a way to condense cases?

def addNegabinary(arr1, arr2):
    result = []
    # Need to start on the highest order bits as they represent the smallest numbers
    i = len(arr1)
    j = len(arr2)
    if i > 0:
        i -= 1
    if j > 0:
        j -= 1
    flag = int(0)
    maxarr = int(0)
    if i > j:
        maxarr = 1
    else:
        maxarr = 2
    carry = int(0)
    while i >= 0 and j >= 0:
        # Many cases
        # case 2 and carry = 0
        if(arr1[i] + arr2[j] == 2) and carry == 0:
            result.append(0)
            carry = -1
        # case 1 and carry = -1
        elif(arr1[i] + arr2[j] == 1) and carry == -1:
            result.append(0)
            carry = 0
        # case 2 and carry = -1
        elif(arr1[i] + arr2[j] == 2) and carry == -1:
            result.append(1)
            carry = 0
        # case 0 and carry = -1
        elif(arr1[i] + arr2[j] == 0) and carry == -1:
            result.append(1)
            carry = 1
        # case 0 and carry = 1
        elif(arr1[i] + arr2[j] == 0) and carry == 1:
            result.append(1)
            carry = 0
        # case 0 and carry = 0
        elif(arr1[i] + arr2[j] == 0) and carry == 0:
            result.append(0)
            carry = 0
        elif(arr1[i] + arr2[j] == 1) and carry == 0:
            result.append(1)
            carry = 0
        #case 1 and carry = 1
        elif(arr1[i] + arr2[j] == 1) and carry == 1:
            result.append(0)
            carry = -1
        # case 2 and carry = 1
        else:
            result.append(1)
            carry = -1
        i -= 1
        j -= 1
        # Once we've gotten here, if lists are uneven that means a list still has values
    if maxarr == 1:
        while i >= 0:
            if arr1[i] == 1 and carry == -1:
                result.append(0)
                carry = 0
            elif arr1[i] == 0 and carry == -1:
                result.append(1)
                carry = 1
            elif arr1[i] == 0 and carry == 0:
                result.append(0)
                carry = 0
            elif arr1[i] == 1 and carry == 1:
                result.append(0)
                carry = -1
            else:
                result.append(1)
                carry = 0
            i -= 1
    elif maxarr == 2:
        while j >= 0:
            if arr2[j] == 1 and carry == -1:
                result.append(0)
                carry = 0
            elif arr2[j] == 0 and carry == -1:
                result.append(1)
                carry = 1
            elif arr2[j] == 0 and carry == 0:
                result.append(0)
                carry = 0
            elif arr2[j] == 1 and carry == 1:
                result.append(0)
                carry = -1
            else:
                result.append(1)
                carry = 0
            j -= 1
    if carry == 1:
        result.append(1)
    if carry == -1:
        result.append(1)
        result.append(1)
    if flag != 1:
        result.reverse()
    # Need to clean up any leading zeros
    while(True):
        if result[0] == 0 and len(result) > 1:
            result.pop(0)
        else:
            break
    return result


def main():
    arr1 = [1]
    arr2 = [1,1,0,1]
    print(addNegabinary(arr1, arr2))


if __name__ == "__main__":
    main()
