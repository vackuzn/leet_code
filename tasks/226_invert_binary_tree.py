from typing import Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self._build_repr("", [self]).strip()
    
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recurse(root)
        #return self.stack(root)

    def stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        stack = [root]
        while len(stack) > 0:
            n = stack.pop()            
            n.left, n.right = n.right, n.left

            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        
        return root
    
    def recurse(self, root):
        if root is None:
            return None
        
        root.left, root.right = self.recurse(root.right), self.recurse(root.left)
        return root


root = to_tree([4,2,7,1,3,6,9])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().invertTree(root))