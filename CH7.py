#a^3 + b^3 = c^3 + d^3
import math

#using int(round) to round to an integer
#This is O(N^3)
# for a in range (1001):
#     for b in range (1001):
#         for c in range (1001):
#             aCubed = math.pow(a,3)
#             bCubed = math.pow(b,3)
#             cCubed = math.pow(c,3)
#             d = int(round(aCubed + bCubed -cCubed))
#             if aCubed + bCubed == cCubed + (d**3):
#                 print ("The values are ", a,b,c,d)
#                 break

#Using dictionaries O(N^2)
# hashTable = {}
# for a in range(1001):
#     for b in range(1001):
#         result = int(round(math.pow(a,3) + math.pow(b,3)))
#         if result in hashTable:
#             hashTable[result].append((a,b)) #append returns None so no assignment required
#         else:
#             hashTable[result] = [(a,b)]
# for list in hashTable.values(): #need to do .values() to iterate over all lists
#     for pair1 in list:
#         for pair2 in list:
#             print (pair1, pair2)

#Checking permutation of a string is in the other string

def permutationFinder (a, b):
    lengthA = len(a)
    origA = list(a)
    indices = []
    permutationCheck = origA.copy() #need to copy to prevent modifying original
    index = 0
    for letterB in b:
        if letterB in permutationCheck:
            permutationCheck.remove(letterB)
            for i in range (lengthA - 1):
                checkIndex = index + i + 1
                if checkIndex < len(b): #avoid issues where you exceed len(B)
                    if b[checkIndex] in permutationCheck:
                        permutationCheck.remove(b[checkIndex])
                        if len (permutationCheck) == 0:
                            indices.append(index)
                            permutationCheck = origA.copy() #need to reset permutationChecker once found
                    else:
                        permutationCheck = origA.copy()
                        break
        index +=1
    return indices
a = 'abbc'
b= 'cbabadcbbabbcbabaabccbabc'
# print(len(b))
# print (permutationFinder (a,b))
#Note slice works form (start, stop - 1, step) with stop - 1 as default parameter

#Example: Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique.
a = "abcd"
print(a[slice(1,2)])
from itertools import permutations
#note, permutations will returns tuples in case of a list or string passed in
def printAllStringPermutations (a):
    perms = [''.join(p) for p in permutations(a)] #This is list comprehension
    print(perms) # to remove duplicates

#2sorted arrays, find number of common elements
#Approach 1, use hashtabels

import array
def num_of_common_elements(a,b):
    hashTable = {}
    count = 0
    for element in a:
        hashTable[element] = 1
    for element in b:
        if element in hashTable: #how to check hashTable for that key
            count +=1
    return count
a = array.array('f', [13,27,35,40,49,55,59])
b = array.array('f', [17, 35, 39, 40, 55, 58, 60])
print (num_of_common_elements(a,b))

#Approach 2, taking advantage of sorted arrays
def num_of_common_elements_v2(a,b):
    indexb = 0
    count = 0
    for element in a:
        for i in range(indexb, len(b)):
            if b[i] == element:
                count += 1
                indexb = i
    return count

print (num_of_common_elements_v2(a,b))

#adding two polynomial equations together

class monomial:
    def __init__(self, coefficient = None, power = None):
        self.coeff = coefficient
        self.power = power

    def get_coefficient(self):
        return self.coeff
    def get_power(self):
        return self.power

#assuming distinct monomials
def add_two_polynomials (exprA, exprB):
    result = []
    for monomialA in exprA:
        for monomialB in exprB:
            powerA = monomialA.get_power()
            powerB = monomialB.get_power()
            if powerA == powerB:
                coefficientA = monomialA.get_coefficient()
                coefficientB = monomialB.get_coefficient()
                monomialR = monomial(coefficientA + coefficientB, powerA)
                result.append(monomialR)
    return result

#better runtime using hashtables

def add_two_polynomials (exprA, exprB):
    results = {}
    addedExpr = []
    for monomialA in exprA:
        powerA = monomialA.get_power()
        coeffA = monomialA.get_coefficient()
        results[powerA] =  coeffA
    for monomialB in exprB:
        powerB = monomialB.get_power()
        if powerB in results:
            results[powerB] = results[powerB] + monomialB.get_coefficient()
    for power in results:
        monomialR = monomial(results[power],power)
        addedExpr.append(monomialR)
    return addedExpr






