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

#TODO: Review this solution
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

# print (one_away ("pale", "ale"))

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

#90 degree right rotation is transpose and hflip
#90 degree left rotation is transpose and vflip
import numpy as np
#this one works for MxN and not just NxN
def rotate_matrix(matrix):
    original__matrix = matrix.copy()
    refactored = []
    zeros = []
    orig_rows = len(matrix)
    orig_columns = len(matrix[0])
    for i in range(orig_rows): #make sure to draw on paper for ease
        zeros.append(0)
    for i in range(orig_columns):
        new = zeros.copy()
        refactored.append(new)
    for row in range(orig_rows): #This is essentially a transpose
        for column in range(orig_columns):
            refactored[column][row] = matrix[row][column]
    for row in refactored:
        row.reverse()
    return refactored


# print (rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8]]))

#TODO: practice on an in place version of the rotations
def rotate_matrix_using_np (matrix):
    matrix = np.transpose(matrix)
    matrix = np.flip(matrix, axis = 1)
    return matrix
#Learnings: numpy operations require assignment while no assignment for list.reverse() and list.append()
#axs = 0 is vertical, 1 is horizontal
# test = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print (rotate_matrix_using_np(test))

def zero_matrix(matrix):
    row_index = 0
    indices = []
    for row in matrix:
        column_index = 0
        for column in row:
            if column == 0:
                indices.append((row_index, column_index))
            column_index +=1
        row_index +=1
    for row,column in indices:
        matrix[row, :] = 0
        matrix[:,column] = 0
    return matrix
# test_zero = np.array([[1,2,0,4],[5,6,7,8]])
# print (zero_matrix(test_zero))
#Learning: Indexing entire rows and columns for a numpy array

#can check using the in operator
def string_rotation(s1,s2):
    repeated = s2 + s2
    if s1 in repeated:
        return True
    else:
        return False

print(string_rotation("waterbottle", "erbottlewat"))
# print(string_rotation("waterbottle", "erbottlewst"))

# def rotate_matrix_in_place(matrix):
