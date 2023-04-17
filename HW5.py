def selection_sort(arr):
    for i in range(len(arr)):
        x = i
        for j in range(len(arr)):
            if arr[x] < arr[j]:
                arr[x], arr[j] = arr[j], arr[x]
    return arr


def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return split_and_sort(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def split_and_sort(left, right):
    ordered_arr = []
    i = j = 0
    while i < len(left) or j < len(right):
        if len(left) == i:
            ordered_arr.append(right[j])
            j = j + 1
            continue
        if len(right) == j:
            ordered_arr.append(left[i])
            i = i + 1
            continue
        if left[i] <= right[j]:
            ordered_arr.append(left[i])
            i = i + 1
        else:
            ordered_arr.append(right[j])
            j = j + 1
    return ordered_arr
        

test_list = [3, 5, 1, 6, 2]
print(f'selection sort: {selection_sort(test_list)}')
test_list = [3, 5, 1, 6, 2]
print(f'bubble sort: {bubble_sort(test_list)}')
test_list = [3, 5, 1, 6, 2]
print(f'insertion sort: {insertion_sort(test_list)}')
test_list = [3, 5, 1, 6, 2]
print(f'merge sort: {merge_sort(test_list)}')