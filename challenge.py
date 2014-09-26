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


def main():
    wordlist = read_wordlist()


if __name__ == '__main__':
    main()

