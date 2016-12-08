from math import sqrt, floor


def sum_of_dividers(num):

    result = 0
    for i in xrange(1, min(int(floor(sqrt(num))) + 1, num)):
        if num % i == 0:
            result += i
            other = num / i
            if other != i:
                result += (num / i)

    return result


def solve_first(limit):

    index = 1
    presents = 1
    while presents < limit:

        index += 1
        presents = sum_of_dividers(index) * 10

    return index


def sum_of_dividers2(num, houses):

    result = 0
    for i in xrange(1, min(int(floor(sqrt(num))) + 1, num)):
        if num % i == 0:
            if i * houses >= num:
                result += i

            other = num / i
            if other * houses >= num and other != i:
                result += (num / i)

    return result


def solve_second(limit, houses):

    index = 1
    presents = 1
    while presents < limit:

        index += 1
        presents = sum_of_dividers2(index, houses) * 11

    return index


print solve_first(100)  # 6
print solve_first(70)  # 4
print solve_first(150)  # 8
print solve_first(29000000)

print solve_second(29000000, 50)
