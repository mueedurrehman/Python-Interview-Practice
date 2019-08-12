
memo_ts = {}
def triple_step(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if n not in memo_ts:
            memo_ts[n] = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
        return memo_ts[n]

# print(triple_step(5))
#Logic: if n = 4. Permutations of 3 get you to 3. Adding 1 is unique
#Permutations of 2 get you to 2. Adding 2 is unique
#Permutations of 1 get you to 1, Adding 1 is unique

#Values are distinct
#So at midpoint if no match
def magic_index(array):
    midpoint = len(array) // 2
    mid_element = array[midpoint]
    if mid_element == midpoint:
        return midpoint
    elif mid_element > midpoint:
        return magic_index (array[:midpoint])
    else:
        return magic_index(array[midpoint + 1:])

#If elements are not distinct
#Cannot deduce anything from the midpoint
def magic_index_repetitive(array):
    for index, element in enumerate(array):
        if index == element:
            return index

#Note: You are adding to the same list you are iterating over
#Simple solution is to use a copy to iterate
def power_set_iter(set):
    perms = [[]]
    for element in set:
        for subset in perms.copy():
            perms.append(subset + [element])
    return perms
# print(power_set_iter([1,2,3]))

def power_set_recur(set):
    def recur_builder(set, accu):
        if len(set) == 0:
            return accu
        else:
            for element in accu.copy():
                accu.append(element + [set[0]])
            return recur_builder(set[1:], accu)
    return recur_builder(set, [[]])

# print (power_set_recur([1,2,3]))

def recursive_multiply(a,b):
    def recursive_helper(a,b,accu):
        if b == 1:
            return accu
        elif b % 2 == 0:
            return recursive_helper(a, b >> 1, accu << 1)
        else:
            return recursive_helper(a, b - 1, accu + a)
    return recursive_helper(a,b,a)

# print(recursive_multiply(7,8))

# def tower_of_hanoi(tower1, tower2, tower3):

#ToDo: Do this recursively
#Learning: Cast to set and return so that you get the list without duplicates
def permutations_without_dups(string):
    perms = [""]
    for char in string:
        for element in perms.copy():
            perms.append(element + char)
    return perms
#learning: When constructing permutations or powersets, your storing list must contain the empty string or empty list
# print(permutations_without_dups("abcdd"))

def permutations_with_dups(string):
    perms = [""]
    for char in string:
        for element in perms.copy():
            perms.append(element + char)
    return set(perms)

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

#Note: In this problem, order does not matter
#In the stepping problem, order did matter
# def coins(n):
#     def recursive_helper(coins, denom):
#         if coins > 25:
#             coins (n//25, [10,5,1]) + coins (n)
    # if n < 5:
    #     return 1
    # elif n == 5:
    #     return 2
    # elif n < 10:
    #     return coins(n-5) + coins(n-1)
    # elif n == 10:
    #      return coins(n-5) + coins(n-1) + 1
    # elif n < 25:
    #      return coins(n-5) + coins(n-10) + coins(n-1)
    # else:
    #     return coins(n-25) + coins(n-5) + coins(n-10) + coins(n-1)

# coins = memoize(coins)
#15 should give 6, 10 should give 4
print(coins(15))

