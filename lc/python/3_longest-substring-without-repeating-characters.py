# Given the problem,
# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def length_of_longest_substring(s):
    # Solution function goes here
    # Using Sliding Windows Approach
    kv = set()
    charlist= [x for x in s]
    l , res = 0,0
    for k,v in enumerate(charlist):
        while v in kv:
            kv.remove(charlist[l])
            l+=1
        
        kv.add(v)   # add item to kv
        res = max(res,k-l+1)
    return res

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
    (" ", 1),
    ("abcdefg", 7),
    ("aab", 2),
    ("dvdf", 3),
    ("tmmzuxt", 5),
    ("aabaab!bb", 3)
])
def test_length_of_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected