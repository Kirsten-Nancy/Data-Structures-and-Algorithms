count_dict = {}

def first_unique_character(string):
    for char in string:
        if char not in count_dict:
            # Add the character as key to the dictionary with a value of 1
            count_dict[char] = 1
        else:
            # Increment the count
            count_dict[char] += 1

    for key, val in count_dict.items():
        if val == 1:
            # Loop through the dictionary items and find first key with val==1 then find it's index in the string
            return string.index(key)
    # return count_dict


my_string = 'leetcode'
print(first_unique_character(my_string))

