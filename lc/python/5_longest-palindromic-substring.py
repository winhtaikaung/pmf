# Given the problem,
# https://leetcode.com/problems/longest-palindromic-substring/

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def longest_palindrome(s):
    # Solution function goes here
    n = len(s)
    start = 0
    end = 1
 
    for i in range(n):
        # Find the longest palindromic substring of even length
        low,hi = i - 1,i
        
 
        while low >= 0 and hi < n and s[low] == s[hi]:
            if hi - low + 1 > end:
                start = low
                end = hi - low + 1
            low -= 1
            hi += 1
 
        # Find the longest palindromic substring of odd length
        low = i - 1
        hi = i + 1
        
        while low >= 0 and hi < n and s[low] == s[hi]:
            
            if hi - low + 1 > end:
                start = low
                end = hi - low + 1
            low -= 1
            hi += 1
    



    return s[start:start+end]
    pass

@pytest.mark.parametrize("s, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a"),
    ("bb", "bb"),
    ("abcba", "abcba"),
    ("aaaa", "aaaa"),
    ("abcde", "a"),
    ("", ""),
    ("racecar", "racecar"),
    ("abba", "abba")
])
def test_longest_palindrome(s, expected):
    assert longest_palindrome(s) == expected