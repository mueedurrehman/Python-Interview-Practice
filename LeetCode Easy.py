def romanToInt(s):
    roman_mappings_uncon = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    roman_reg = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for roman, value in roman_mappings_uncon.items():
        while roman in s:
            s = s.replace(roman, "", 1)  # s.replace RETURNS A COPY OF THE STRING
            result += value
    for char in s:
        result += roman_reg[char]
    return result

# print(romanToInt("IV"))


def longestSubstring(s):
    characters = {}
    repetitions = []
    for index, char in enumerate(s):
        if char not in characters:
            characters[char] = [index]
        else:
            characters[char].append(index)
    max_difference = 0
    start = 0
    end = 0
    for values in characters.values():
        length = len(values)
        if length > 1:
            for i in range(length - 1):
                difference = values[i + 1] - values[i]
                if difference > max_difference:
                    max_difference = difference
                    start = max(values[i] - 1, 0)
                    end = values[i + 1]
    if max_difference == 0:
        return len(s)
    else:
        return len(s[start:end])

# print(longestSubstring("pwwkew"))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1:
            current = ListNode(l1.val)
            head = current
            l1 = l1.next
        elif l2:
            current = ListNode(l2.val)
            head = current
            l2 = l2.next
        while l1 and l2:
            current.next = ListNode(l1.val)
            l1 = l1.next
            current = current.next
            current.next = ListNode(l2.val)
            # current = current.next LOOK AT THIS PATTERN. CURRENT WILL GET ASSIGNED TO A COMPLETELY NEW OBJECT HERE
            # current = ListNode(l2.val)
            l2 = l2.next
            current = current.next
        while l1:
            current = ListNode(l1.val)
            l1 = l1.next
            current = current.next
        while l2:
            current = ListNode(l2.val)
            l2 = l2.next
            current = current.next
        return head


# Works but is a slow implementation
def isUgly(self, num: int) -> bool:
    if num < 1:
        return False
    elif num == 1:
        return True
    else:
        if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
            return False
        print("here")
        limit = round(num // 2)
        iter = 7
        while (iter <= limit):
            if num % iter == 0:
                divisor = iter
                print(divisor)
                while divisor > 1:
                    if divisor % 2 == 0:
                        divisor = divisor / 2
                    elif divisor % 3 == 0:
                        divisor = divisor / 3
                    elif divisor % 5 == 0:
                        divisor = divisor / 5
                    else:
                        return False
            iter += 2
        return True


def isUgly(self, num: int) -> bool:
    if num < 1:
        return False
    elif num == 1:
        return True
    else:
        if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
            return False
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        if num == 1:
            return True
        return False

def mySqrt(x):
    if x < 2:
        return x
    left = 2
    right = x // 2
    while (left <= right):
        guess = (left + right) // 2
        squared = guess * guess
        if squared < x:
            left = guess + 1
        elif squared > x:
            right = guess - 1
        else:
            return guess #It is a perfect square
    return right #return the integer square root that is less than

# print(mySqrt(9))

def reversebin(n):
    binary = bin(n)[2:]
    reversed = binary[::-1]
    print(reversed)
    return int(reversed,2)

# print (reversebin(int("00000010100101000001111010011100", 2)))

def maxProduct(nums):
    start = 0
    end = 0
    if nums == []:
        return None
    product = None
    max_product = None
    while end < len(nums):
        nxt = nums[end]
        if product is not None:
            product = product * nxt
        else:
            product = nxt
        if max_product is None:
            max_product = product
        if product > max_product:
            max_product = product
        if product < 0 and (end == len(nums) - 1 or nums[end + 1] == 0):
            while start < end:
                remove = nums[start]
                product = product / remove
                if product > max_product:
                    max_product = product
                start += 1
        elif product == 0:
            start = end + 1
            product = None
        end += 1
    return int(max_product)

# print(maxProduct([-2,0,-1]))

# print(list("abcdef"))

#Look at conditions
#The deadline is strictly greater than the previous start
#and <= previous deadline
#The start is >= previous start but less than next deadline
def meeting_rooms_one(meetings):
    no_conflict = []
    for new in meetings:
        for previous in no_conflict:
            if new[1] > previous[0] and new[1] <= previous[1] or new[0] >= previous[0] and new[1] < previous[1]:
                return False
        no_conflict.append(new)
    return True

# print (meeting_rooms_one([[1,4],[5,6],[8,9],[2,6]]))

def meeting_rooms_log(meetings):
    meetings = sorted(meetings, key = lambda x: x[0])
    for i in range(1,len(meetings)):
        if meetings[i][0] < meetings[i - 1][1]:
            return False
    return True

# print (meeting_rooms_log([[1,4],[5,6],[12,13],[7,11]]))

def meeting_rooms_required(meetings):
    times = []
    for meeting in meetings:
        times.append((meeting[0],'s'))
        times.append((meeting[1],'d'))
    times = sorted(times, key = lambda x : x[0])
    counter = 0
    max = 0
    for item in times:
        if item[1] == 's':
            counter +=1
            if counter > max:
                max = counter
        else:
            counter -=1
    return max

# print (meeting_rooms_required([[1,4],[5,6],[12,13],[7,11]]))
list1 = [1,2,3]
list1[0:0].append(1)
print(list1[2:])