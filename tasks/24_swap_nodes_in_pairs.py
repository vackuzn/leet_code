from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: "ListNode" = next
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # add fake header node
        if head is None:
            return None
        
        fake_head = ListNode(0, head)

        prev_node = fake_head
        while prev_node is not None:
            n1 = prev_node.next if prev_node is not None else None
            n2 = n1.next if n1 is not None else None
            n3 = n2.next if n2 is not None else None

            if n2 is None:
                break
            
            prev_node.next = n2
            n1.next = n3
            n2.next = n1

            prev_node = n1
        
        return fake_head.next

        
head = to_ll([1,2,3,4])
head = to_ll([])
head = to_ll([1])
head = to_ll([1,2,3])
print(Solution().swapPairs(head))


# 2 pointers, second starts after 1st does n steps. when p1 reaches end, p2 should be pointing to node before the one we need