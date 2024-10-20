from collections import defaultdict
from typing import Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        if root is None:
            return []
        
        entries = defaultdict(int)
        duplicates = []
        
        def calc_repr(n: TreeNode) -> str:
            repr = f"({n.val}"
            if n.left:
                repr += "l" + calc_repr(n.left)
            if n.right:
                repr += "r" + calc_repr(n.right)
            repr += ")"

            entries[repr] += 1

            if entries[repr] == 2:
                duplicates.append(n)

            return repr
        
        calc_repr(root)

        return duplicates


root = to_tree([4,2,7,1,3,6,2])
root = to_tree([2,1,1])
root = to_tree([2,2,2,3,None,3,None])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().findDuplicateSubtrees(root))