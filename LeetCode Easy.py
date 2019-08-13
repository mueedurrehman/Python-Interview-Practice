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
