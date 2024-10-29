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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # min number of nodes = 2 -> root is never 0

        # Morris alg
        prev_val = None
        min_diff = None

        tourist = root
        while tourist is not None:
            if tourist.left:
                guide = tourist.left
                while guide.right and guide.right != tourist:
                    guide = guide.right

                if guide.right is None:
                    # Left path unvisited, create bridge
                    guide.right = tourist
                    tourist = tourist.left

                elif guide.right == tourist:
                    # Left path already visited, destroy bridge and move to right
                    guide.right = None

                    # Perform in order traversal
                    if prev_val is not None:
                        abs_diff = abs(tourist.val - prev_val)
                        min_diff = abs_diff if min_diff is None else min(min_diff, abs_diff)
                    
                    prev_val = tourist.val
                    tourist=tourist.right               
            else:                
                # Perform in order traversal
                if prev_val is not None:
                    abs_diff = abs(tourist.val - prev_val)
                    min_diff = abs_diff if min_diff is None else min(min_diff, abs_diff)
                
                prev_val = tourist.val
                tourist=tourist.right

        return min_diff


root = to_tree([2,7,153])
#root = to_tree([1,2,3,4,None,5,6,None,None,7])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().getMinimumDifference(root))