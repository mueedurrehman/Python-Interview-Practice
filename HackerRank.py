#Goldman Sachs Hacker Rank Test

# def rotateTheString(originalString, direction, amount):
#     length = len(originalString)
#     for index, direc in enumerate(direction):
#         amt = amount[index]
#         if amt > length:
#             while (amt > length):
#                 amt = amt % length
#         if direc == 1:
#             while amt > 0:
#                 originalString = originalString[-1] + originalString[:-1]
#                 amt -=1
#         elif direc == 0:
#             while amt > 0:
#                 originalString = originalString[1:] + originalString[0]
#                 amt -=1
#     return originalString
#
# string1 = rotateTheString("abc", [0], [3])
# # string = rotateTheString("hurart", [0,1], [4,1])
# print(string1)
#
# def is_prime(number):
#     if number == 1:
#         return False
#     iter = 2
#     while iter*iter <= number:
#         if number % iter == 0:
#             return False
#         iter += 1
#     return True
import timeit


def is_prime(number):
    if number == 1:
        return False
    iter = 2
    while iter * iter <= number:
        if number % iter == 0:
            return False
        iter += 1
    return True

def is_prime_v2(number):
    if number <= 1 or number % 2 == 0:
        return False
    if number == 2:
        return True
    iter = 3
    test_limit = round(number**0.5)
    while iter <= test_limit:
        if number % iter == 0:
            return False
        iter += 2
    return True
number = 10000007
# print(number**0.5)
# print(round(number**0.5))
# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#     return wrapped
# number = 10000007
# wrapped = wrapper(is_prime, number)
# wrapped2 = wrapper(is_prime_v2, number)
# print (timeit.timeit(wrapped, number = 1000))
# print (timeit.timeit(wrapped2, number = 1000))
# for i in range(1, 1000000):
#     if is_prime(i) != is_prime_v2(i):
#         print(i)
#         print ("My prime does not work")
# print("Done")

# def is_prime

# def spiralOrderPrimes(grid):
#     # Write your code here
#     primes = []
#     def is_prime(number):
#         if number == 1:
#             return False
#         iter = 2
#         while iter*iter <= number:
#             if number % iter == 0:
#                 return False
#             iter += 1
#         return True
#     row_index = 0
#     column_index = 0
#     max_column = len(grid[0])
#     max_row = len(grid)
#     spiral = []
#     while row_index < max_row and column_index < max_column:
#         for i in range(column_index, max_column):
#             spiral.append(grid[row_index][i])
#         row_index +=1
#         for i in range(row_index, max_row):
#             spiral.append(grid[i][max_column - 1])
#         max_column -=1
#         if row_index < max_row:
#             for i in range(max_column - 1, column_index - 1, -1):
#                 spiral.append(grid[max_row -1][i])
#             max_row -= 1
#         if column_index < max_column:
#             for i in range(max_row - 1, row_index - 1, -1):
#                 spiral.append(grid[i][column_index])
#             column_index +=1
#     # print (spiral)
#     primes = filter(is_prime, spiral)
#     return primes


# while row_index < max_row and column_index < max_column:
#         for i in range(column_index, max_column):
#             number = grid[row_index][i]
#             if is_prime(number):
#                 primes.append(number)
#         row_index +=1
#         for i in range(row_index, max_row):
#             number = grid[i][max_column - 1]
#             if is_prime(number):
#                 primes.append(number)
#         max_column -=1
#         if row_index < max_row:
#             for i in range(max_column - 1, column_index - 1, -1):
#                 number = grid[max_row -1][i]
#                 if is_prime(number):
#                     primes.append(number)
#             max_row -= 1
#         if column_index < max_column:
#             for i in range(max_row - 1, row_index - 1, -1):
#                 number = grid[i][column_index]
#                 if is_prime(number):
#                     primes.append(number)
#             column_index +=1
