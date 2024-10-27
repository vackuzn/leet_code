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
    def connect(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root is None:
            return None
        
        cur_level = [root]
        next_level = []

        while len(cur_level) > 0:
            prev = None
            for node in cur_level:
                if prev:
                    prev.next = node
                
                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

                prev = node
            
            cur_level = next_level
            next_level = []
        
        return root
    
    def connect_queue(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root is None:
            return None
        
        q = deque([root])
        while len(q) > 0:
            # 1 BFS level
            level_node_count = len(q)
            for i in range(level_node_count):
                node = q.popleft()

                if i < level_node_count - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
        
        return root
    

root = to_tree([3,9,20,None,None,15,7])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().connect(root))