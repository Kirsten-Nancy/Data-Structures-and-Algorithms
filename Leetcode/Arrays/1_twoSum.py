#  TODO: Implement using hashmap, target-currentValue
def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

mylist = [3,2,4]
target = 6

print(twoSum(mylist, target))
