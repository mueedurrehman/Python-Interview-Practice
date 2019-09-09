#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getAutocompleteScores' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY documentTitles
#  2. STRING_ARRAY documentBodies
#  3. STRING_ARRAY queries
#
# import string


def getAutocompleteScores(documentTitles, documentBodies, queries):
    scores = {}
    # Parsing the text and storing scores in a dictionary (hashtable) for quick lookup
    for title in documentTitles:
        words = title.split()
        for word in words:
            # Tried removing punctuation
            # word = word.translate(str.maketrans('', '', string.punctuation))
            # word = word.strip()
            # if word != "":
            if word not in scores:
                scores[word] = 10
            else:
                scores[word] += 10

    for body in documentBodies:
        words = body.split()
        for word in words:
            # word = word.translate(str.maketrans('', '', string.punctuation))
            # word = word.strip()
            # if word != "":
            if word not in scores:
                scores[word] = 1
            else:
                scores[word] += 1

    # Building a trie to provide the autocomplete suggestions:
    class trie_node:
        def __init__(self):
            self.children = {}
            self.last = False

    class trie:
        def __init__(self):
            self.root = trie_node()
            self.word_list = []

        def add(self, word):
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = trie_node()
                node = node.children[ch]
            node.last = True

        def formTrie(self, words):
            for word in words:
                self.add(word)

        def suggestions_build(self, node, word):
            if node.last:
                self.word_list.append(word)

            for ch, n in node.children.items():
                self.suggestions_build(n, word + ch)

        def suggestionsList(self, word):
            node = self.root
            temp = ""
            for ch in word:
                if ch not in node.children:
                    return None
                temp += ch
                node = node.children[ch]
            self.suggestions_build(node, temp)
            return self.word_list

    words = trie()
    words.formTrie(scores.keys())  # Add all of the words to the trie for autocomplete purposes
    answers = []
    # Caching queries for efficiency in case of a repeat query
    cache = {}
    for query in queries:
        if query not in cache:
            ac_result = words.suggestionsList(query)
            # Query cannot autocomplete to anything. Result is 0.
            if ac_result is None:
                answers.append(0)
            else:
                # Find the maximum score among all autocomplete possibilities for the query
                max_score = 0
                for word in ac_result:
                    cur_score = scores[word]
                    if cur_score > max_score:
                        max_score = cur_score
                answers.append(max_score)
                cache[query] = max_score
            words.word_list = []  # resetting the trie's word_list for the next query
        else:
            answers.append(cache[query])
    return answers



titles = ["12345"]
body = ["123456"]
query = [""]

print(getAutocompleteScores(titles, body, query))