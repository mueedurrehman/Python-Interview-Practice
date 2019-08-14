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

string1 = "abc"
string2 = string1
string1 = string1 + "pie"
print(string1)
print(string2)