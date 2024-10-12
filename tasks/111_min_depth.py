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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root)

    def stack(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        min_depth = None
        stack = [(root, 0)]

        while len(stack) > 0:
            cur, cur_depth = stack.pop()
            cur_depth += 1

            is_leaf_node = cur.left is None and cur.right is None
            if is_leaf_node:
                min_depth = cur_depth if min_depth is None else min(min_depth, cur_depth)
            else:
                if cur.right:
                    stack.append((cur.right, cur_depth))        
                if cur.left:
                    stack.append((cur.left, cur_depth))
        
        return min_depth
    
    def recurse(self, root: Optional[TreeNode]) -> int:
        def get_depth(node, cur_depth):
            cur_depth += 1

            present_nodes = []
            if node.left:
                present_nodes.append(node.left)

            if node.right:
                present_nodes.append(node.right)

            if len(present_nodes) == 0:
                return cur_depth

            return min([get_depth(n, cur_depth) for n in present_nodes])
        
        if root is None:
            return 0
        
        return get_depth(root, 0)


root = to_tree([3,9,20,None,None,15,7])
root = to_tree([2, None, 3, None, 4, None, 5, None, 6])
#root = to_tree([3,9,20])
#root = to_tree([1,2,3]); targetSum = 5
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().minDepth(root))

# As we need to remove all nodes with duplicate value, resulting list may be empty, so add fake node at start
# We will need to have pointer to prev node to update ref, current node and next to compare values
# If cur.value = next.value then remove all nodes with that value
# else - advance 3 pointers