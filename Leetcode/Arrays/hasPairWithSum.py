array = [1, 2, 3, 4]

total = 6

# Time O(n^2) Space O(1)
def has_pair_with_sum(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == total:
                return True
    return False


# print(has_pair_with_sum(array))

# Time complexity O(n), space-O(n) to store extra data structure
def has_pair_with_sum_set(arr):
    hash_set = set()
    for num in arr:
        if num in hash_set:
            return True
        else:
            # Add the complement of that number to set so that
            # if it is later found along the list we know that there's a number before
            # added to that is equal to the total given
            hash_set.add(total-num)
    return False


print(has_pair_with_sum_set(array))