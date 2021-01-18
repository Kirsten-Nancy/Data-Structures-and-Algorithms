array1 = [0, 3, 4, 4, 31]
array2 = [4, 6, 30]
sorted_array = []

def merge_sorted_arrays(nums1, nums2):
    i = 0
    j = 0

    if len(nums1) == 0:
        return nums2

    elif len(nums2) == 0:
        return nums1

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sorted_array.append(nums1[i])
            i += 1
        else:
            sorted_array.append(nums2[j])
            j += 1

    # If one element has more elements
    while i < len(nums1):
        print(f'i: {i}')
        sorted_array.append(nums1[i])
        i += 1

    while j < len(nums2):
        print(f'j: {j}')
        sorted_array.append(nums2[j])
        j += 1

    return sorted_array


def merge_sorted_array2(nums1, nums2, no_elem_nums1, no_elem_nums2):
    if len(nums1) == 0:
        return nums2
    if len(nums2) == 0:
        return nums1

    i = no_elem_nums1 - 1
    j = no_elem_nums2 - 1
    k = no_elem_nums1 + no_elem_nums2 - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 3, 4]
# Do i know the number of elements in each list
m = 3
n = 3
print(merge_sorted_array2(arr1, arr2, m, n))
# print(merge_sorted_arrays(array1, array2))



# Method3
# array1.extend(array2)
# array1.sort()
# print(array1)