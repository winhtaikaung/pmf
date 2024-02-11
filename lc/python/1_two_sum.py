# Given the problem,
# https://leetcode.com/problems/two-sum

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def two_sum(nums, target):
    # Solution function goes here
    nums.sort()
    i = 0
    j = len(nums) -1 
    while(i<j):
        res = nums[i] + nums[j]
        print(nums[i] + nums[j])
        if res == target:
            return [i,j]
        elif res < target:
            i = i+1
        else:
            j = j-1


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([0, 1, 2, 3, 4, 5], 9, [4, 5]),
    ([2,5,5,11], 10,[1,2])

])
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected