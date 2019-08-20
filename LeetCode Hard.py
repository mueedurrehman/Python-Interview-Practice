def minWindow(s,t):
    count = {}
    total_chars = 0  # Do not use length as may have greater for one char. Use this to know when all char counts <= 0
    for char in t:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            total_chars += 1
    left = 0
    right = 0
    length = len(s)
    max_len = None
    answer = ""
    while right < length:
        next = s[right]
        if next in count:
            count[next] -= 1
            if count[next] == 0:
                total_chars -= 1
                while total_chars == 0:
                    check = s[left]
                    if check not in count:
                        left += 1
                    else:
                        if count[check] < 0:
                            left += 1
                            count[check] += 1
                        elif count[check] == 0:
                            new_answer = s[left: right + 1]
                            new_length = len(new_answer)
                            if max_len is None or new_length < max_len:
                                max_len = new_length
                                answer = new_answer
                            left += 1
                            count[check] += 1
                            total_chars += 1
        right += 1
    return answer

# print(minWindow ("ADOBECODEBANC", "ABC"))

# def findSubstring(words, s):
#     p = ''.join(words)
#     count = {}
#     word_hash = {}
#     total_words = 0
#     for word in words:
#         if word in word_hash:
#             word_hash[word] += 1
#         else:
#             word_hash[word] = 1
#             total_words += 1
#     total_chars = 0
#     for char in p:
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#             total_chars += 1
#     start = 0
#     end = 0
#     length = len(p)
#     total_length = len(s)
#     indices = []
#     while end < total_length:
#         next = s[end]
#         if next in count:
#             count[next] -= 1
#             if count[next] == 0:
#                 total_chars -= 1
#                 if total_chars == 0:  # total_chars can only be zero when you have achieved window length
#                     anagram = s[start: end + 1]
#                     s_check = 0
#                     e_check = 0
#                     tmp_total_words = total_words
#                     word_copy = word_hash.copy()
#                     while e_check < len(anagram):
#                         word = anagram[s_check: e_check + 1]
#                         if word in word_copy:
#                             word_copy[word] -= 1
#                             s_check += len(
#                                 word)  # words may not necessarily be unique so change length outside incrementing total words
#                             if word_copy[word] == 0:
#                                 tmp_total_words -= 1
#                         e_check += 1
#                     if tmp_total_words == 0:
#                         indices.append(start)
#         window_length = end + 1 - start
#         if window_length == length:  # moving fixed size window
#             remove = s[start]
#             if remove in count:  # character may not need to be removed
#                 if count[remove] == 0:  # Removed character is required to make anagram
#                     total_chars += 1  # Only change total chars when exact number of removed characters as required for anagram so removing one means no longer an anagram
#                 count[remove] += 1
#             start += 1
#         end += 1
#     return indices




def findSubstring(words, s):
    if len(words) < 1:
        return []
    word_hash = {}
    total_words = 0
    for word in words:
        if word in word_hash:
            word_hash[word] += 1
        else:
            word_hash[word] = 1
            total_words += 1
    word_hash_tmp = word_hash.copy()
    total_words_tmp = total_words
    total_length = len(s)
    word_length = len(words[0])
    start = 0
    next_check = 0
    end = word_length
    indices = []
    found_index = False
    while end <= total_length: #if no + 1 indexing, then end <= total_length is the required condition
        potential = s[next_check: end]  # Note here we do not need the + 1 indexing as we are adding the length required to end. If end is just a pointer, then we need + 1 as start and end both begin at 0
        if potential in word_hash_tmp:
            word_hash_tmp[potential] -= 1
            if word_hash_tmp[potential] == 0:
                total_words_tmp -= 1
                del word_hash_tmp[potential]
                if total_words_tmp == 0:
                    found_index = True
            if not found_index:
                next_check += word_length
                end += word_length
            else:
                indices.append(start)
                total_words_tmp = total_words
                word_hash_tmp = word_hash.copy()
                start += 1
                end = start + word_length
                next_check = start
                found_index = False
        else:
            total_words_tmp = total_words
            word_hash_tmp = word_hash.copy()
            start += 1
            end = start + word_length  # check from next index onwards
            next_check = start
    return indices

print(findSubstring(["word","good","best","good"],"wordgoodgoodgoodbestword"))

def longestSubstring2Distinct(s):
    characters = {}
    total_chars = 0
    start = 0
    end = 0
    answer = ""
    max_length = 0
    while end < len(s):
        nxt = s[end]
        if nxt not in characters:
            characters[nxt] = 1
            total_chars += 1
        else:
            characters[nxt] += 1
        while total_chars > 2:
            remove = s[start]
            characters[remove] -= 1
            if characters[remove] == 0:
                del characters[remove]
                total_chars -= 1
            start += 1
        cur_length = end + 1 - start
        if cur_length > max_length:
            max_length = cur_length #either update max_length or compute every time with len
            answer = s[start:end + 1]
        end += 1
    return answer

def longestSubstringKDistinct(s, k):
    characters = {}
    total_chars = 0
    start = 0
    end = 0
    answer = ""
    max_length = 0
    while end < len(s):
        nxt = s[end]
        if nxt not in characters:
            characters[nxt] = 1
            total_chars += 1
        else:
            characters[nxt] += 1
        while total_chars > k:
            remove = s[start]
            characters[remove] -= 1
            if characters[remove] == 0:
                del characters[remove]
                total_chars -= 1
            start += 1
        cur_length = end + 1 - start
        if cur_length > max_length:
            max_length = cur_length #either update max_length or compute every time with len
            answer = s[start:end + 1]
        end += 1
    return answer

print (longestSubstring2Distinct("abcbbbbcccbdddddddddddddddddaadacb"))
print (longestSubstringKDistinct("abcadcacacaca", 3))


# def characterReplacement(self, s: str, k: int) -> int:
# characters = {}
#         total_replacements = 0
#         start = 0
#         end = 0
#         current = ""
#         total_chars = 0
#         max_length = 0
#         length = len(s)
#         while end < length
#             if character in characters:
#                 characters[char] +=1
#             else:
#                 characters[char] = 1
#                 if total_chars > 1:
#                     nxt =
#                 total_chars +=1
#         while end < length:
#             nxt = s[end]
#             if nxt not in characters:
#                 characters[nxt] = 1
#                 total_replacements = 0
#             else:
#                 characters[nxt] += 1
#             cur_length = end + 1 - start
#             if cur_length > max_length:
#                 max_length = cur_length
#                 answer = s[start: end + 1]
#         return answer