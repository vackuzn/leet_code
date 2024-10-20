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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root)

    def recurse(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def rec(node: TreeNode, cur_depth: int) -> tuple[int, int]:
            if node.left is None and node.right is None:
                return (cur_depth, cur_depth)
            
            mn = None
            mx = None

            if node.left:
                mn, mx = rec(node.left, cur_depth + 1)

            if node.right:
                r_min, r_max = rec(node.right, cur_depth + 1)
                mn = r_min if mn is None else min(mn, r_min)
                mx = r_max if mx is None else max(mx, r_max)
            
            return (mn, mx)
        
        mn, mx = rec(root, 1)

        return mx - mn <= 1

    def dfs_stack(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        dfs_stack = [(root, 1)]
        depths = set()

        while len(dfs_stack) > 0:
            cur, depth = dfs_stack.pop()
            if cur.left is None and cur.right is None:
                depths.add(depth)

            if cur.left:
                dfs_stack.append((cur.left, depth + 1))

            if cur.right:
                dfs_stack.append((cur.right, depth + 1))

        return max(depths) - min(depths) <= 1


root = to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
root = to_tree([3,9,20,None,None,15,7])
#root = to_tree([1,2,2,3,3,None,None,4,4])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().isBalanced(root))