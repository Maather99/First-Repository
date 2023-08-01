#to find the sum of two numbers in the list is eequal to target 9

nums=[2,7,6,9]
target=9
def twoSum(n):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i]== target:
                return [i, j]
                


print("The sum of the index", twoSum(nums), "is equal to 9")