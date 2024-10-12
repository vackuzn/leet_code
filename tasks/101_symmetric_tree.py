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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #return self.recurse(root)
        return self.stack_dfs(root)

    def recurse(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric(n1, n2):
            if n1 is None and n2 is None:
                return True
            
            if n1 is None or n2 is None:
                return False
            
            if n1.val != n2.val:
                return False
            
            return is_symmetric(n1.left, n2.right) and is_symmetric(n1.right, n2.left)
        
        if root is None:
            return True
        
        return is_symmetric(root.left, root.right)

    def stack_bfs(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        cur_layer = [(root.left, root.right)]
        next_layer = []

        while len(cur_layer) > 0:
            for n1, n2 in cur_layer:
                if n1 is None and n2 is None:
                    continue

                if n1 is None or n2 is None:
                    return False
                
                if n1.val != n2.val:
                    return False
                
                next_layer.append((n1.left, n2.right))
                next_layer.append((n1.right, n2.left))

            cur_layer = next_layer
            next_layer = []

        return True
    
    def stack_dfs(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        stack = [(root.left, root.right)]
        
        while len(stack) > 0:
            n1, n2 = stack.pop()
            
            if n1 is None and n2 is None:
                continue

            if n1 is None or n2 is None:
                return False
            
            stack.append((n1.left, n2.right))
            stack.append((n1.right, n2.left))

        return True


root = to_tree([1,2,2])
root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().isSymmetric(root))