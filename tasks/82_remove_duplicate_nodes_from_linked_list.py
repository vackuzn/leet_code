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
        
        ghost_node = ListNode(0, head)

        prev = ghost_node
        value_to_remove = None

        while prev.next:
            cur = prev.next
            next = cur.next

            if cur.val == value_to_remove:
                prev.next = next
                continue
            else:
                value_to_remove = None
            
            if next and cur.val == next.val:
                value_to_remove = cur.val
                prev.next = next
                continue

            prev = cur
        
        return ghost_node.next
            


l = to_ll([1,2,1,3])
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().deleteDuplicates(l))

# As we need to remove all nodes with duplicate value, resulting list may be empty, so add fake node at start
# We will need to have pointer to prev node to update ref, current node and next to compare values
# If cur.value = next.value then remove all nodes with that value
# else - advance 3 pointers