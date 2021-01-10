nums = [0,1,2,2,3,0,4,2]
value = 2

# Allocated extra space for abother array
# def removeEl(array,val):
#     copyArray = nums.copy()
#     for num in copyArray:
#         if num == val:
#             array.remove(num)
#     return array

# length = len(nums)

# def removeEl(array,val):
#     for val in array:
#         print(val)
#         array.remove(val)
#     return array

# print(removeEl(nums,value))
# This works because it does not depend on the length of array like the for loop doe
while value in nums:
    print('Before removal',nums)
    nums.remove(value)
    print('After removal',nums)

