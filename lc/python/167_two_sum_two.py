# Given the problem,
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def two_sum(numbers, target):
    # Solution function goes here
    if len(numbers) == 0:
        return []
    l = 0
    r = len(numbers) - 1
    
    while l<r:
        res = numbers[l] + numbers[r]

        if res < target:
            l+=1
        elif res > target:
            r-=1
        else:
            
            return [l+1,r+1]
            
    pass

@pytest.mark.parametrize("numbers, target, expected", [
    # ([2, 7, 11, 15], 9, [1, 2]),
    ([-2, 0, 3, 6, 7, 9], 7, [2, 4]),
    # ([1, 2, 3, 4, 5], 9, [4, 5]),
    # ([0, 0, 0, 0], 0, [1, 2]),
    # ([-5, -4, -3, -2, -1], -8, [2, 4]),
    # ([], 5, []),
])
def test_two_sum(numbers, target, expected):
    assert two_sum(numbers, target) == expected