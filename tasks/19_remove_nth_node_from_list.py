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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fake_head = ListNode(0, head)

        p1 = fake_head
        p2 = fake_head
        p1_steps = 0

        while True:
            p1 = p1.next
            p1_steps += 1

            if p1_steps > n:
                p2 = p2.next

            if p1.next is None:
                p2.next = p2.next.next
                break
        
        return fake_head.next

        
head = to_ll([1,2,3,4,5]); n = 2
head = to_ll([1]); n = 1
head = to_ll([1,2]); n = 1
#l1 = to_ll([0]); l2 = to_ll([0]) # result: 0
#l1 = to_ll([9,9,9,9,9,9,9]); l2 = to_ll([9,9,9,9]) # result: 0

print(Solution().removeNthFromEnd(head, n))


# 2 pointers, second starts after 1st does n steps. when p1 reaches end, p2 should be pointing to node before the one we need