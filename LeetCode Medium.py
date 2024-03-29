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

# print(setZeroes([[1],[0]]))

def maxOccurrenceChar(hashtable):
    return max(hashtable.values())

# print (maxOccurrenceChar({1:9,2:0}))


def characterReplacement(self, s: str, k: int) -> int:
    characters = {}
    total_entries = 0
    total_replacements = 0
    start = 0
    end = 0
    current = ""
    total_chars = 0
    max_length = 0
    length = len(s)
    while end < length:
        nxt = s[end]
        if nxt in characters:
            characters[nxt] += 1
            total_entries += 1
        else:
            characters[nxt] = 1
            total_chars += 1
            total_entries += 1
        total_replacements = maxOccurrenceChar(characters) - total_entries
        while total_replacements > k:
            remove = s[start]
            characters[remove] -= 1
            total_entries -= 1
            if characters[remove] == 0:
                total_chars -= 1
                del characters[remove]
            total_replacements = maxOccurrenceChar(characters) - total_entries
            start += 1
        cur_length = end + 1 - start
        if cur_length > max_length:
            max_length = cur_length
            # answer = s[start: end + 1]
        end += 1
    return max_length

def threeSum(nums):
    if len(nums) < 3:
        return []
    solutions = []
    length = len(nums)
    hashtable = {}
    for integer in nums:
        if integer not in hashtable:
            hashtable[integer] = 1
        else:
            hashtable[integer] += 1
    for i in range(length - 2):
        for j in range(i + 1,length - 1):
            pair_neg = -(nums[i] + nums[j])
            if pair_neg in hashtable:
                if nums[i] == nums[j] and hashtable[nums[i]] == 1:
                    continue
                if nums[j] == pair_neg and hashtable[nums[j]] == 1:
                    continue
                if nums[i] == pair_neg and hashtable[nums[i]] == 1:
                    continue
                if nums[i] == pair_neg and nums[j] == pair_neg and hashtable[nums[i]] < 3:
                    continue
                result = [nums[i], nums[j], pair_neg]
                result.sort()
                if result not in solutions:
                    solutions.append(result)
    return solutions

# print(threeSum([-2,0,0,2,2]))


def numIslands(grid):
    stack = []
    rows = len(grid)
    columns = len(grid[0])
    islands = 0
    def dfs_walk(coord):
        stack.append(coord)
        nonlocal islands
        while stack != []:
            coord = stack.pop()
            r = coord[0]
            c = coord[1]
            grid[r][c] = None
            if r != rows - 1 and grid[r + 1][c] == "1":
                stack.append((r+1,c))
            if r != 0 and grid[r - 1][c] == "1":
                stack.append((r - 1,c))
            if c != 0 and grid[r][c - 1] == "1":
                stack.append((r,c-1))
            if c != columns - 1 and grid[r][c + 1] == "1":
                stack.append((r,c+1))
        print(grid)
        islands +=1
    for r in range(rows):
        for c in range(columns):
            if grid [r][c] == "1":
                dfs_walk((r,c))
    return islands
# list1 = [["1","1","1"],["0","1","0"],["0","1","0"]]

def friend_circles(M):
        length = len(M)
        visited = [False] * length
        stack = []
        circles = 0
        def dfs_walk(friend):
            stack.append(friend)
            nonlocal circles
            while stack != []:
                nonlocal length
                friend = stack.pop()
                visited[friend] = True
                for i in range(length):
                    if M[friend][i] == 1 and visited[i] == False:
                        stack.append(i)
            circles += 1
        for r in range(length):
            if not visited[r]:
                dfs_walk(r)
        return circles

# print(friend_circles([[1,1,0],[1,1,0],[0,0,1]]))

def topKFrequent(nums, k):
    counts = {}
    max_freq = 0
    for element in nums:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1
        if counts[element] > max_freq:
            max_freq = counts[element]
    #[[]] using this to initialize means internal lists point to the same object
    frequency = [ [] for i in range(max_freq)]
    for key, freq in counts.items():
        target = frequency[freq - 1]
        target.append(key)
    output = []
    for i in range(1, len(frequency) + 1):
        if k != 0 and frequency[-i] != []:
            for item in frequency[-i]:
                output.append(item)
                k -= 1
                if k == 0:
                    return output
        else:
            return output

print(topKFrequent([3,0,1,0], 1))