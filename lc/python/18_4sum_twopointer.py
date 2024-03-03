# Given the problem,
# https://leetcode.com/problems/4sum/description/

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def four_sum(nums, target):
    # Solution function goes here
    if len(nums) == 0:
        return []
    nums.sort()

    pairs = []

    for x in range(len(nums)-3):
        if x > 0 and nums[x] == nums[x-1]:
            continue

        for i in range(x+1,len(nums)-2):
            if i > x+1 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) -1 
            while l < r:
                result = nums[l] + nums[r] + nums[i]+nums[x]
                if result < target:
                    l+=1
                elif result > target:
                    r -=1
                else:
                    pairs.append([ nums[l] , nums[r] ,nums[i],nums[x]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                            l+=1

    print(pairs)
    return pairs
    pass

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    # ([], 0, []),
    # ([1, 2, 3, 4, 5], 10, []),
    # ([1, 2, 3, 4, 5], 7, [[1, 2, 3, 1]]),
    # ([1, 2, 3, 4, 5], 9, [[1, 2, 3, 3], [1, 2, 4, 2], [1, 3, 5, 0], [2, 3, 4, 0]]),
    # ([-1, -2, -3, -4, -5], -9, [[-5, -4, -3, -1]]),
    # ([-1, -2, -3, -4, -5], -7, [[-5, -2, -3, 3], [-4, -3, -2, 2], [-5, -4, -2, 4], [-5, -3, -2, 3]]),
    # ([0, 0, 0, 0], 0, [[0, 0, 0, 0]])
])
def test_four_sum(nums, target, expected):
    assert four_sum(nums, target) == expected