def string_has_all_unique (input):
    list = []
    for element in input:
        list.append(element)
    if len (list) == len (input):
        return True
    else:
        return False

#Attempt 2 without using additional data structures. Requires O(N^2) time in worst case
def string_has_all_unique_v2 (input):
    for element in input:
        if input.count(element) > 1:
            return False

    return True

#TODO: Develop non itertools solution
def checkPermutation(a,b):
    if len(a) != len (b):
        return False
    from itertools import permutations
    perms = [''.join(p) for p in permutations(b, len (b)) ]
    if a in perms:
        return True
    else:
        return False
#version without using itertools
def checkPermutation_V0 (a,b):
    if len(a) != len (b):
        return False
    elems_a = {}
    for element in a:
        elems_a[element] = True
    for element in b:
        if element not in elems_a:
            return False
    return True #Note return true outside as every element needs to be checked

# a = "abcdefg"
# b  =  "gfedcab"
# print (checkPermutation_V0(a,b))

#URLify:
def urlify (input):
    return input.replace(' ', '%20')

# print (urlify("a d s c"))

#Palindrome Permutation. NOTE: Assuming no special characters else just strip them out
#If there are other special characters, we can remove all of them using regex
def palindrome_checker (input):
    hashTable = {}
    input = input.replace(' ','')
    input = input.lower()
    is_odd = False
    if len(input) % 2 == 1:
        is_odd = True
    for letter in input:
        if letter in hashTable:
            hashTable[letter] += 1
        else:
            hashTable[letter] = 1
    for count in hashTable.values():
        if (not is_odd) and count % 2 != 0: #even number of non-space characters
            return False
        elif count % 2 != 0:
            is_odd = False
    return True
#Learning: string.replace(oldvalue, newvalue, count) method
# print (palindrome_checker('Able was I ere I saw Elba'))

#Definitely good solution
def one_away(a,b):
    totalEdits = 0
    letters = []
    difference = abs(len(a) - len (b))
    if difference >= 2:
        return False
    elif difference == 1:
        if len (a) > len (b):
            longer = a
            shorter =b
        else:
            longer = b
            shorter = a
        for element in longer:
            letters.append(element)
        index = 0
        for element in shorter:
            compared = letters[index]
            if compared != element:
                test = longer.replace(compared, '', 1)
                if test != shorter:
                    return False
                else:
                    return True
            index +=1
        return True
    elif difference == 0:
        for element in a:
            letters.append(element)
        index = 0
        for element in b:
            if letters[index] != element:
                totalEdits +=1
                if totalEdits >= 2:
                    return False
            index += 1
        return True

print (one_away ("pale", "ale"))

#Error 1: Need to add element when repetitions added as for loop advances
#Error 2: Need to have a method for adding in the last elements
def string_compression(uncompressed):
    index = 0
    compressed = ""
    repetitions = 0
    previous = ''
    for element in uncompressed:
        if element == previous:
            repetitions += 1
        elif repetitions > 1:
                compressed = compressed + str(repetitions) + element
                repetitions = 1
        else:
            compressed = compressed + element
            repetitions = 1
            # else:
            #     compressed = compressed + repetitions
        previous = element
    if repetitions > 1:
        compressed = compressed + str (repetitions)
    return compressed
# Learnings: Need to cast integers to strings
# print (string_compression("aabdcccccaaa"))

def rotate_matrix(matrx):
