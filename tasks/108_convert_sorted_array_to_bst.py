from typing import Optional
from collections import deque


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)
    
    def _build_repr(self, s: str, level_nodes: list["TreeNode"]):
        next_nodes = []
        s_level = ""
        level_empty = True

        for n in level_nodes:
            if not n:
                s_level += "None "
            else:
                level_empty = False
                s_level += str(n.val) + " "
                next_nodes.append(n.left)
                next_nodes.append(n.right)

        if level_empty:
            return s
        
        return self._build_repr(s + "\n" + s_level, next_nodes)


def to_tree(arr: list[int]) -> TreeNode:
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while i < len(arr):
        current = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])

        def build_tree(start, end) -> TreeNode:
            if start > end:
                return None
            
            middle_idx = (end + start) // 2

            node = TreeNode(nums[middle_idx])
            node.left = build_tree(start, middle_idx - 1)
            node.right = build_tree(middle_idx + 1, end)

            return node
        
        return build_tree(0, len(nums) - 1)


nums = [2,7,153]
#root = to_tree([1,2,3,4,None,5,6,None,None,7])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().sortedArrayToBST(nums))