# Given the problem,
# https://leetcode.com/problems/longest-palindromic-substring/

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def longest_palindrome(s):
    # Solution function goes here
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