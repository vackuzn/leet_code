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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ghost_node = ListNode(0, head)
        # find first occurrence of node with value >= x
        x_prev = ghost_node
        while x_prev.next:
            if x_prev.next.val >= x:
                break
            x_prev = x_prev.next
        else:
            # reached end of list - no changes needed
            return head

        # start search till the end of list while moving nodes with val < x before x_cur
        x_next = x_prev.next

        prev = x_next
        cur = prev.next
        while cur:
            next = cur.next
            if cur.val < x:
                # put cur node after x_prev
                x_prev.next = cur
                cur.next = x_next
                x_prev = cur

                # update pointer after extraction
                prev.next = next
                cur = next
            else:
                prev = cur
                cur = next
        
        return ghost_node.next


l = to_ll([1,4,3,2,5,2]); x = 3
l = to_ll([2,1]); x = 2
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().partition(l, x))

# As we need to remove all nodes with duplicate value, resulting list may be empty, so add fake node at start
# We will need to have pointer to prev node to update ref, current node and next to compare values
# If cur.value = next.value then remove all nodes with that value
# else - advance 3 pointers