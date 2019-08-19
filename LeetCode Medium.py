def lengthOfLongestSubstring(self, s: str) -> int:
    substring = ""
    characters = {}
    length = len(s)
    max_length = ""
    for index, char in enumerate(s):
        for i in range(index, length):
            if s[i] in characters:
                characters = {}
                if len(substring) > len(max_length):
                    max_length = substring
                substring = ""
                break
            else:
                characters[s[i]] = 1
                substring = substring + s[i]
        if len(substring) > len(max_length):
            max_length = substring
    print(max_length)
    return len(max_length)

def lengthOfLongestSubstring(self, s: str) -> int:
    # O(n) solution
    length = len(s)
    if length < 2:
        return length
    letters = {}
    max_length = 0
    start = 0
    for i in range(length):
        char = s[i]
        if char in letters:
            start = max(letters[char] + 1, start)
        letters[char] = i
        new_len = i - start + 1
        max_length = max(new_len, max_length)
    return max_length

# print(lengthOfLongestSubstring("abcabcbb"))

# string1 = "abc"
# string2 = string1
# string1 = string1 + "pie"
# print(string1)
# print(string2)


def letterCombinations(digits):
    keys = {"1": [], "0": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
            "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    base = []
    for char in digits:
        base.append(keys[char])
    permutations = [""]
    for lst in base:
        for element in permutations.copy():
            for char in lst:
                new_element = element + char
                permutations.append(new_element)
    return [word for word in permutations if len(word) == len(digits)]

# print(letterCombinations("23"))


#Ugly iterative solution. Works but TLE.
def isUgly(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return False
    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    if n == 1:
        return True
    return False


def nthUglyNumber(n: int) -> int:
    ugly = 0
    i = 1
    while (ugly < n):
        if isUgly(i):
            ugly += 1
        i += 1
    return i - 1

# nthUglyNumber(1)

def subsets (nums):
    sets = [[]]
    for item in nums:
        for element in sets.copy():
            sets.append(element + [item])
    return sets
print(subsets([1,2,3]))


def setZeroes(matrix):
    # Find the first zero. Use that for storage purposes
    rows = len(matrix)
    columns = len(matrix[0])
    # The goal is to save extra iterations
    # If you mark a zero as None and then iterate over all rows and columns = Extra iterations
    # If you mark a zero's first row and first column as None and then iterate, you are still getting extra iterations
    first_col = False
    for r in range(0, rows):
        for c in range(0, columns):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                if c == 0:  # If the column was the first column, then additional variable. Must correspond with later erase
                    first_col = True
                else:
                    matrix[0][c] = 0
    print(matrix)
    for r in range(1, rows):
        for c in range(1, columns):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    # Need separate variable
    print(matrix)
    if matrix[0][0] == 0:
        for c in range(1, columns):
            matrix[0][c] = 0
    if first_col:
        for r in range(0, rows): #Need this to be from 0 to solve [1],[0] case
            matrix[r][0] = 0

print(setZeroes([[1],[0]]))