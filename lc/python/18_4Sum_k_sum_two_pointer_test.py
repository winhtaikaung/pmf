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
    quad = []

    def kSum(k,start,target):
        if k != 2:
            for i in range(start,len(nums)-k+1):
                if i> start and nums[i] == nums[i-1] :
                    continue
                quad.append(nums[i])
                kSum(k-1,i+1,target-nums[i])
                quad.pop()
            return
        
        l = start
        r = len(nums) - 1
        
        while (l<r):
            result = nums[l] + nums[r]
            if result > target:
                r-= 1
            elif result < target:
                l+=1
            else:
                pairs.append(quad+[nums[l],nums[r]])
                l+=1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
                
    kSum(4,0,target)
    # print(pairs)
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