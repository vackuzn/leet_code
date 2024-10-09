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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        prev = head
        while prev.next:
            cur = prev.next
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
        
        return head


l = to_ll([1,1,2,3,3])
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().deleteDuplicates(l))

# start from first node, if next node value equals to prev, remove next node, if not equals - advance