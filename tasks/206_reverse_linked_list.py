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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return self.iterative(head)
        return self.recursive(None, head)
    
    def iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 or 1 items
        if head is None or head.next is None:
            return head
        
        prev = None
        cur = head
        
        while cur is not None:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        return prev

    def recursive(self, prev: Optional[ListNode], cur: Optional[ListNode]) -> Optional[ListNode]:
        if cur is None:
            return cur

        next = cur.next
        cur.next = prev

        if next is None:
            return cur
        
        return self.recursive(cur, next)

        
l = to_ll([1,2,3,4,5])
#l = to_ll([1,2])
#l = to_ll([])

print(Solution().reverseList(l))