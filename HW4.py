def even_first(arr):
    a = 0
    for i in range(0, len(arr)):
        if arr[a] % 2 != 0:
            arr.insert(len(arr), arr.pop(a))
        if arr[a] % 2 == 0:
            a = a + 1
    return arr


def increment_up(arr):
    length = len(arr)
    last_number = arr[-1]
    if last_number != 9:
        arr[-1] = arr[-1] + 1
        return arr
    if last_number == 9:
        count = -1
        while arr[count] == 9:
            count = count - 1
        arr[count] = arr[count] + 1
        for i in range(1, len(arr)):
            if arr[i] == 9:
                arr[i] = 0
        return arr


test_list = [1, 5, 2, 7, 4, 7, 9]
print(even_first(test_list))

test_list1 = [3, 2, 1]
test_list2 = [4, 3, 9]
test_list3 = [5, 9, 9, 9]
print(increment_up(test_list1))
print(increment_up(test_list2))
print(increment_up(test_list3))
