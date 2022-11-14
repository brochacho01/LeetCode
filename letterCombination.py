letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g','h','i'], ['j','k', 'l'], ['m', 'n', 'o'], ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
def letterCombinations(digits):
    # Driver code
    combinations = []
    for i in range(len(letters[charInt(digits[0])])):
        dfs(0, i, digits, "", combinations)
    return combinations

#imagine each number in digits as a layer in a tree. i.e. first num is the first level etc
def dfs(setNum, setPos, digits, curString, combinations):
    # Append letter from current position and level to string
    curString+=letters[charInt(digits[setNum])][setPos]
    # If on last level, append string to combinations and return
    if setNum == (len(digits) - 1):
        combinations.append(curString)
        return 
    # else continue recursing down the tree
    for i in range(len(letters[charInt(digits[setNum + 1])])):
        dfs(setNum + 1, i, digits, curString, combinations)

# simple function to turn chars into indexes of our letters list by 
def charInt(char):
    return (ord(char) - 50)

def main():
    digits ="23"
    letterCombinations(digits)

if __name__ == "__main__":
    main()
