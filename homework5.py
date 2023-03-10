def sum_of_digits(n):
    sum = 0
    for num in range(1, n+1):
        sum = sum + num
    return sum


def max_num(num1, num2, num3):
    return max(num1, num2, num3)


def odd_even_digits(number):
    digits = [int(x) for x in str(number)]
    even = 0
    odd = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd


print(sum_of_digits(10))
print(max_num(20,40,200))
print(odd_even_digits(12345))
