array = [2, 5, 1]
hash_set = set()

def first_recurring_character(arr):
    if len(arr) == 0:
        return None
    for char in arr:
        if char in hash_set:
            return char
        else:
            hash_set.add(char)
    return None


print(first_recurring_character(array))