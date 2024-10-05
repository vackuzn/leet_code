from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ('' if self.next is None else str(self.next))


def to_ll(nums: list[int]) -> ListNode:
    head = None
    prev = None

    for d in nums:
        cur = ListNode(d)
        if head is None:
            head = cur

        if prev:
            prev.next = cur

        prev = cur

    return head

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        result_curr = None
        carry = False

        while l1 or l2 or carry:
            current = 1 if carry else 0
            carry = False

            if l1:
                current += l1.val
                l1 = l1.next
            
            if l2:
                current += l2.val
                l2 = l2.next
            
            carry = current > 9
            current %= 10

            if result_head is None:
                result_head = ListNode(current)
                result_curr = result_head
            else:
                result_curr.next = ListNode(current)
                result_curr = result_curr.next                

        return result_head

        
#l1 = to_ll([2, 4, 3]); l2 = to_ll([5, 6, 4]) # result: 807
#l1 = to_ll([0]); l2 = to_ll([0]) # result: 0
#l1 = to_ll([9,9,9,9,9,9,9]); l2 = to_ll([9,9,9,9]) # result: 0
l1 = to_ll([2,4,9]); l2 = to_ll([5,6,4,9]) # result: [7,0,4,0,1]

print(Solution().addTwoNumbers(l1, l2))