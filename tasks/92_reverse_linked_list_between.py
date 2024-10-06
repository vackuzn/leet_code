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
        
        ghost_node = ListNode(0, head)
        prev = ghost_node
        
        # Advance to start of sublist
        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next

        # Reverse sublist
        before_sublist = prev

        # cur and before_sublist variables remain unchanged in contrast with full list reversal algorithm
        # we move cur from left to right, circularly moving nodes from cur's right to sublist start, like a snake game
        for _ in range(right - left):
            node_right = cur.next                 # node we move from cur's right to start of sublist

            cur.next = node_right.next            # step over next: cur -- (bypass node_right) --> node_right.next
            node_right.next = before_sublist.next # point node_right.next to the start of sublist
            before_sublist.next = node_right      # point before_sublist.next to the new sublist start - node_right
        
        return ghost_node.next


l = to_ll([1,2,3,4,5]); left = 2; right = 4
l = to_ll([1,2,3,4,5]); left = 1; right = 5
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().reverseBetween(l, left, right))