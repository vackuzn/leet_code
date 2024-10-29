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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.morris(root)
    
    def morris(self, root) -> bool:
        tourist = root
        prev_min = None
        
        while tourist is not None:
            if tourist.left:
                # One step left and max to the right
                guide = tourist.left
                while guide.right is not None and guide.right != tourist:
                    guide = guide.right
                
                # dead end - create bridge
                if guide.right is None:
                    guide.right = tourist
                    tourist = tourist.left
                    continue
                
                # already visited - right is tourist - delete bridge and
                if guide.right == tourist:
                    guide.right = None

                    # in order traversal for tourist
                    if prev_min is not None and prev_min >= tourist.val:
                        return False
                    
                    prev_min = tourist.val
                    tourist = tourist.right
            else:
                # in order traversal for tourist
                if prev_min is not None and prev_min >= tourist.val:
                    return False
                
                prev_min = tourist.val
                tourist = tourist.right

        return True
    
    def recurse_inorder(self, root: Optional[TreeNode]) -> bool:
        local_min = None

        def is_valid_bst(node):
            if node is None:
                return True

            nonlocal local_min

            # left branch
            if not is_valid_bst(node.left):
                return False
            
            # node
            if local_min is not None and node.val <= local_min:
                return False

            local_min = node.val

            # right branch
            if not is_valid_bst(node.right):
                return False

            return True
        
        return is_valid_bst(root)


    def recurse_dfs_min_max(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(node: TreeNode | None, min_boundary: int | None = None, max_boundary : int | None = None):
            if node is None:
                return True

            # Node value lies within boundaries
            if min_boundary is not None and node.val <= min_boundary:
                return False

            if max_boundary is not None and node.val >= max_boundary:
                return False

            # Immediate children adhere to BST requirement
            if node.left and node.left.val >= node.val:
                return False

            if node.right and node.right.val <= node.val:
                return False

            # Traverse child nodes
            return is_valid_bst(node.left, min_boundary, node.val) and is_valid_bst(node.right, node.val, max_boundary)
        
        return is_valid_bst(root)


root = to_tree([2,1,3])
root = to_tree([1,2,3,4,None,5,6,None,None,7])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().isValidBST(root))