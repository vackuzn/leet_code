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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs
        # if leaf node - check if sum == target : return true
        # if not leaf - pass partial sum to nested DFS
        #return self.recursive(root, targetSum)
        return self.iterative(root, targetSum)

    def recursive(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _path_sum(node: Optional[TreeNode], path_sum: int):
            if node is None:
                return False
            
            path_sum += node.val
            is_leaf_node = node.left is None and node.right is None
            if is_leaf_node:
                return path_sum == targetSum
            
            return _path_sum(node.left, path_sum) or _path_sum(node.right, path_sum)
        
        return _path_sum(root, 0)
    
    def iterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        # use stack
        cur = root
        stack = []
        part_sum = 0

        while True:
            part_sum += cur.val

            is_leaf_node = cur.left is None and cur.right is None
            if is_leaf_node:
                if part_sum == targetSum:
                    return True
            
                if len(stack) == 0:
                    return False
            
                cur, part_sum = stack.pop()
            else:
                if cur.left and cur.right:
                    stack.append((cur.right, part_sum))
                    cur = cur.left
                else:
                    cur = cur.left if cur.left else cur.right


root = to_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]); targetSum = 22
#root = to_tree([1,2,3]); targetSum = 5
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().hasPathSum(root, targetSum))

# As we need to remove all nodes with duplicate value, resulting list may be empty, so add fake node at start
# We will need to have pointer to prev node to update ref, current node and next to compare values
# If cur.value = next.value then remove all nodes with that value
# else - advance 3 pointers