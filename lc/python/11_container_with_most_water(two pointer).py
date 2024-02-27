# Given the problem,
# https://leetcode.com/problems/container-with-most-water

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def max_area(h):
    # Solution function goes here
    l = 0
    r=  len(h)-1
    area = 0

    while l<r :
        area = max(area,min(h[l] ,h[r]) * (r-l))
        
        if(h[l] < h[r]):
            l+=1
        else:
            r-=1

    return area
    
    

@pytest.mark.parametrize("height, expected", [
    # ([1,8,6,2,5,4,8,3,7], 49),
    # ([1,1], 1),
    # ([4,3,2,1,4], 16),
    # ([1,2,1], 2),
    # ([1,2,4,3], 4),
    # ([1,1,1,1,1], 4),
    # ([1,2,3,4,5,6,7,8,9,10], 25),
    # ([10,9,8,7,6,5,4,3,2,1], 25),
    ([2,3,10,5,7,8,9], 28)
])
def test_max_area(height, expected):
    assert max_area(height) == expected