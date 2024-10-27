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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.bfs_list(root)

    def bfs_list(self, root: Optional[TreeNode]) -> int:
        cur_level = [root]
        next_level = []
        leftmost_val = root.val

        while cur_level:
            leftmost_val = cur_level[0].val
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)
                
            cur_level = next_level
            next_level = []
        
        return leftmost_val

    def dfs(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        max_level = 1
        bottom_left_node_value = root.val

        while stack:
            node, level = stack.pop()

            # left first DFS
            if node.right:
                stack.append((node.right, level + 1))

            if node.left:
                stack.append((node.left, level + 1))

            if level > max_level:
                max_level = level
                bottom_left_node_value = node.val
        
        return bottom_left_node_value
    

root = to_tree([2,1,3])
root = to_tree([1,2,3,4,None,5,6,None,None,7])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().findBottomLeftValue(root))