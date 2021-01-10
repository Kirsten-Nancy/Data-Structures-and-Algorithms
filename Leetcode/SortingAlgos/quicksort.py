array = [5, 4, 3, 2, 1]
# The Quicksort function


def quick_sort(a, left, right):
    if left < right:
        q = partition(a, left, right)
        quick_sort(a, left, q - 1)
        quick_sort(a, q + 1, right)


def partition(a, l, r):
    # Last element as pivot
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        print(i)
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


print(array)
quick_sort(array, 0, len(array)-1)
print(array)