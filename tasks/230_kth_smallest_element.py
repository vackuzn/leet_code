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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #return self.dfs_recurse(root, k)
        #return self.dfs_recurse_1(root, k)
        return self.dfs_stack(root, k)
        #return self.morris(root, k)

    def morris(self, root: Optional[TreeNode], k: int) -> int:
        # root cannot be none by conditions
        tourist = root

        while tourist:
            if tourist.left:
                guide = tourist.left
                while guide.right and guide.right != tourist:
                    guide = guide.right
                
                if guide.right is None:
                    guide.right = tourist
                    tourist = tourist.left
                    continue
                
                if guide.right == tourist:
                    guide.right = None

                    k -= 1
                    if k == 0:
                        return tourist.val
                    
                    tourist = tourist.right
            else:
                k -= 1
                if k == 0:
                    return tourist.val

                tourist = tourist.right
    
    def dfs_recurse(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node: Optional[TreeNode]):
            if node:
                yield from helper(node.left)
                yield node.val
                yield from helper(node.right)
        
        for val in helper(root):
            k -= 1
            if k == 0:
                return val
    
    def dfs_recurse_1(self, root: Optional[TreeNode], k: int) -> int:
        def traverse_bst(node: Optional[TreeNode]) -> list[int]:
            result = [node.val]
            
            if node.left:
                result = traverse_bst(node.left) + result
            
            if node.right:
                result = result + traverse_bst(node.right)
            
            return result

        return traverse_bst(root)[k-1]
    
    def dfs_stack(self, root: Optional[TreeNode], k: int) -> int:
        stack = [(root, False)]

        while stack:
            node, left_visited = stack.pop()

            if not left_visited:
                # 1. left path
                while node:
                    stack.append((node, True))
                    node = node.left
                continue
            else:
                # 2. process node
                k -= 1
                if k == 0:
                    return node.val
                
                if node.right:
                    stack.append((node.right, False))
                


            




root = to_tree([3,1,4,None,2]); k=1
#root = to_tree([5,3,6,2,4,None,None,1]); k=3
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().kthSmallest(root, k))
