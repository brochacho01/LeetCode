# Could be sped up by reducing dict.gets
def twoSum(nums, target):
    foundNums = {}
    for i in range(len(nums)):
        curInt = nums[i]
        newTarget = target - curInt
        if (foundNums.get(newTarget,-1) != -1) and (i != foundNums.get(newTarget, -1)):
            return [foundNums.get(newTarget), i]
        else:
            foundNums.update({curInt : i})

def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

if __name__ == "__main__":
    main()