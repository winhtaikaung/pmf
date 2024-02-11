# Given the problem,
# https://leetcode.com/problems/add-two-numbers

# Generate pytest test cases in pytest.mark.parametrize way.

import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    # Solution function goes here
    def reverse_n_int(ll,init_val=[],num=0):
        
        if ll.next == None:
            init_val.append(ll.val)
            init_val.reverse()
            num = int(''.join([str(x) for x in init_val ]))
            return num
            
        else: 
            init_val.append(ll.val)
            return reverse_n_int(ll.next,init_val,num)

    def build_ll_from_int(num):
        if len(num) == 0:
            return None
        ln = ListNode(num[0])
        ln.next = build_ll_from_int(num[1:])
        return ln
    sum = reverse_n_int(l1) + reverse_n_int(l2)

    return build_ll_from_int([int(x) for x in str(sum)])
    

@pytest.mark.parametrize("l1, l2, expected", [
    (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))), ListNode(7, ListNode(0, ListNode(8)))),
    # (ListNode(0), ListNode(0), ListNode(0)),
    # (ListNode(9, ListNode(9, ListNode(9))), ListNode(9, ListNode(9, ListNode(9))), ListNode(8, ListNode(9, ListNode(9, ListNode(1))))),
    # (ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6))), ListNode(5, ListNode(7, ListNode(9)))),
    # (ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), ListNode(9, ListNode(9, ListNode(9))), ListNode(8, ListNode(9, ListNode(9, ListNode(0, ListNode(1)))))),
    # (ListNode(2), ListNode(8, ListNode(9)), ListNode(0, ListNode(0, ListNode(1))))
])
def test_add_two_numbers(l1, l2, expected):
    assert add_two_numbers(l1, l2) == expected