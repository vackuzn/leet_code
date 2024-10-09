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


def to_tree(nums: list[int]) -> TreeNode:
    if len(nums) == 0:
        return None
    
    root_node = TreeNode(nums.pop(0))
    
    bottom_layer = [root_node]
    while nums:
        next_layer = []
        try:
            for n in bottom_layer:
                n.left = TreeNode(nums.pop(0))
                n.right = TreeNode(nums.pop(0))
                
                next_layer.append(n.left)
                next_layer.append(n.right)
        except IndexError:
            break

        bottom_layer = next_layer

    return root_node


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._recurse(root)
        self._stack(root)

    def _recurse(self, root: Optional[TreeNode]) -> None:
        self._move_tree_right_return_tail(root)

    def _move_tree_right_return_tail(self, node: Optional[TreeNode]):
        if not node or (not node.left and not node.right):
            return node
        
        if node.right is None:
            node.right = node.left
            node.left = None
        
        if node.left is None:
            return self._move_tree_right_return_tail(node.right)
        
        flattened_left_branch_end = self._move_tree_right_return_tail(node.left)
        right = node.right
        node.right = node.left
        flattened_left_branch_end.right = right
        node.left = None

        return self._move_tree_right_return_tail(right)
    
    def _stack(self, root: Optional[TreeNode]) -> None:
        right_nodes = []

        cur = root
        while cur:
            if cur.left:
                if cur.right:
                    right_nodes.append(cur.right)
                cur.right = cur.left
                cur.left = None
            if not cur.right and len(right_nodes)>0:
                cur.right = right_nodes.pop()
            cur = cur.right


t = to_tree([1,2,3])
t = to_tree([1,2,5,3,4,None,6])
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

Solution().flatten(t)
print(t)

# use DFS
# self, dfs(left), dfs(right)