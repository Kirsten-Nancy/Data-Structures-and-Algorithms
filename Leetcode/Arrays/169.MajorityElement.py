array = [6, 5, 5]
count_dict = {}

def majority_element(nums):
    for i in range(len(nums)):
        if nums[i] in count_dict:
            count_dict[nums[i]] += 1
        else:
            count_dict[nums[i]] = 1

    for key, val in count_dict.items():
        # The majority element is the element that appears more than ⌊n / 2⌋ times.
        if val > len(nums)//2:
            return key


print(majority_element(array))
# TODO: After learning hashmaps come and review and simplify it