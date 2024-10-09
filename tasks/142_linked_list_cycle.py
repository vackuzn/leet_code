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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = head
        fast = head

        cycle_detected = False

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                cycle_detected = True
                break
        
        if cycle_detected:
            p1 = head
            p2 = fast

            steps_taken = 0 
            while p1 != p2:
                steps_taken +=1
                p1 = p1.next
                p2 = p2.next
            
            return steps_taken

        return None
    
    def blunt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}

        steps = 0
        while head:
            if head in visited:
                return visited[head]
            visited[steps]=head
            steps+=1
        
        return None

l = to_ll([1,2,1,3])
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().detectCycle(l))

# 1. Blunt approach with hashmap
# 2. 2 pointer algorithm