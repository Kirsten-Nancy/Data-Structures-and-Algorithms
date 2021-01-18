input_string = 'nancy'

# Takes extra space, O(n), Time-O(n)
def reverse1(string):
    if string is None:
        return
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]

    return reversed_string


def reverse2(string):
    string_arr = list(string)
    print(string_arr)
    string_arr.reverse()
    print(string_arr)


# reverse2(input_string)


def reverse3(s_list):
    right = len(s_list) - 1
    left = 0
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return s_list


print(reverse3(list(input_string)))