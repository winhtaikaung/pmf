# Given the problem,
# https://leetcode.com/problems/median-of-two-sorted-arrays

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

def find_median_sorted_arrays(nums1, nums2):
    # Solution function goes here
    pass

@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([0, 0], [0, 0], 0.0),
    ([], [1], 1.0),
    ([2], [], 2.0),
    ([], [], None),
    ([1, 3, 5, 7], [2, 4, 6, 8], 4.5),
    ([1, 3, 5], [2, 4, 6, 8], 4.0),
    ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
    ([1, 2, 3, 4], [5, 6, 7], 4.0)
])
def test_find_median_sorted_arrays(nums1, nums2, expected):
    assert find_median_sorted_arrays(nums1, nums2) == expected