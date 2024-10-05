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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        steps_taken = 1
        prev = None
        cur = head
        while steps_taken < left:
            steps_taken += 1
            prev = cur
            cur = cur.next
        
        while steps_taken < right:
            steps_taken += 1
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return head


l = to_ll([1,2,3,4,5]); left = 2; right = 4
#l = to_ll([5])
#l = to_ll([])

print(Solution().reverseBetween(l, left, right))