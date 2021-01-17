# Naive implementation/ Brute force
array1 = ['a', 'b', 'c', 'd']
array2 = [1, 2, 3]

# space O(1), time O(a*b), to account for the different possibility of input lens
def contains_similar_items(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                return True
    return False


# print(contains_similar_items(array1, array2))

# Better approach using hash tables, Space (a), time- O(a+b)
def contains_similar_items_set(arr1, arr2):
    hash_set = set(arr1)
    for i in range(len(arr2)):
        if i in hash_set:
            return True
    return False


print(contains_similar_items_set(array1, array2))