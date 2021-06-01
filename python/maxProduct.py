#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maxProduct(words: [str]) -> int:
    val1, val2 = "", ""

    for word1 in words:
        for word2 in words:
            check = [ letter in word2 for letter in word1 ]
            
            if sum(check) == 0 and word1 != word2:
                #if len(val1) < len(word1):
                #    val1 = word1
                val1 = word1
                if len(val2) < len(word2):
                    val2 = word2

    return val1, val2

if __name__ == "__main__":
    print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
    print(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
    print(maxProduct(["a","aa","aaa","aaaa"]))
