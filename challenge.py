#!/usr/bin/env python
# encoding: utf-8
"""
File Name : challenge.py

Author    : Tony McDaniel
Contact   : tonymcdaniel@gmail.com

Solution to challenge problem posted at
https://github.com/waypaver/Challenge

Copyright (c) 2014 Tony R. McDaniel

"""
import numpy as np


def read_wordlist(infile="randomlist.txt"):
    """
    Read data from `infile` and return a list
    with each line as an element.
    """
    print("Loading wordlist from : "+infile)
    with open(infile,'r') as f:
        wordlist = [ w.strip() for w in f.readlines() ]
    print("Loaded %d words."%len(wordlist))
    return wordlist


def levenshtein_distance(word1, word2):
    """
    Given two strings `word1` and `word2`, returns the Levenshtein distance
    between the two strings. Adapted from the algorithm presented at
    http://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_full_matrix
    """
    m = len(word1)
    n = len(word2)

    # If either word is empty, then the distance is the length
    # of the other word
    if m == 0:
        return n

    if n == 0:
        return m

    # d[i,j] stores the distance from word1[0:i] to word2[0:j]
    # indices of d are i = 0,...,m and j = 0,...n
    d = np.zeros((m+1,n+1),dtype=int)

    # word1 can become the empty string by dropping all letters
    for i in range(m):
        d[i+1,0] = i+1

    # the empty string can become word2 by adding all letters
    for j in range(n):
        d[0,j+1] = j+1

    # loop over the letters of the words to fill the distance matrix
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                d[i+1,j+1] = d[i,j]
            else:
                d[i+1,j+1] = min(d[i,j+1]+1,d[i+1,j]+1,d[i,j]+1)

    # the Levenshtein distance is given by the last entry
    return d[m,n]

def main():
    wordlist = read_wordlist()
    print levenshtein_distance("apple","bananna")


if __name__ == '__main__':
    main()

