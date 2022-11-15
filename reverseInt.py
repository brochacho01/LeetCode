from curses.ascii import isdigit


def reverse(x):
    nonRev = str(x)
    sign = int(0)
    if x > 0:
        sign = 1
    else:
        sign = -1
    rev = nonRev[::-1]
    # Need to check for over/underflow
    # Before doing this, need to check for a negative sign
    isNeg = int(0)
    if not (rev.isdigit()):
        rev = rev.replace('-','')
        isNeg = 1
    revI = int(rev)
    # If the number was negative need to make sure it stays negative
    if isNeg == 1:
        revI -= (revI * 2)
    # Check for overflow and underflow
    if ((revI > 0) and (sign < 0)) or (revI > (2**31) - 1):
        return 0
    elif ((revI < 0) and (sign > 0)) or (revI < (-2**31)):
        return 0
    else:
        return revI

def main():
    x = -123
    print(reverse(x))

if __name__ == "__main__":
    main()