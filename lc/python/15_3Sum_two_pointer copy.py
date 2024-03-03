# Given the problem,
# https://leetcode.com/problems/3sum/description/

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def three_sum(nums):
    # Solution function goes here
    pairs = []
    if (len(nums)==0):
        return pairs
    
    nums.sort() # O(logn) or O(n)
    

    # O(n) x O(n)
    for x in range(len(nums)): #O(n)
        if x > 0 and nums[x] == nums[x-1]:
            continue

        i = x+1
        j = len(nums) -1 

        while i<j : #O(n)
            res = nums[i] + nums[j] + nums[x]
            if res > 0 :
                j-=1
            elif res < 0:
                i+=1
            else:
                pairs.append([nums[i],nums[j],nums[x]])
                i+=1
                while nums[i] == nums[i-1] and i<j:
                    i+=1


        # print(pairs)
    return pairs
    pass

@pytest.mark.parametrize("nums, expected", [
    # ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,0,0,0], [[0,0,0]]),
    # ([], []),
    # ([1,2,3,4,5], []),
    # ([-2,-1,0,1,2,3,4,5], [[-2,-1,3],[-2,0,2],[-1,0,1]]),
    # ([-1,0,1,2,-1,-4,-2,-3,3,0,4], [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]])
])
def test_three_sum(nums, expected):
    assert three_sum(nums) == expected