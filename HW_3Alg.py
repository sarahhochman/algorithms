def find_the_missing_element(arr1, arr2):
    for num in arr1:
        if num not in arr2:
            return num


def largest_sum(arr):
    answer = 0
    holder = 0
    for num in arr:
        holder = answer + num
        if holder >= answer:
            answer = holder
        else:
            number = arr[arr.index(num)+1]
            if (number + holder) >= answer:
                answer = holder
            else:
                return answer
    return answer


def below_mean(arr):
    mean = 0
    for num in arr:
        mean = mean + num
    mean = mean / len(arr)
    print(mean)
    answer = []
    for num in arr:
        if num < mean:
            answer.append(num)
    return answer


def two_lowest(arr):
    arr.sort()
    answer = []
    answer.append(arr[0])
    answer.append(arr[1])
    return answer


try_one = [1, 2, 3, 4, 5]
try_two = [2, 3, 4, 1]
try_three = [43, 45, 47, 49, 51]
try_four = [49, 43, 51, 47]
print(find_the_missing_element(try_one, try_two))
print(find_the_missing_element(try_three, try_four))

try_one = [1, 2, -1, 3, 21, 32, -10, -1]  # 58
print(largest_sum(try_one))

print(below_mean(try_two))
print(below_mean(try_three))
print(below_mean(try_four))

print(two_lowest(try_one))
print(two_lowest(try_two))