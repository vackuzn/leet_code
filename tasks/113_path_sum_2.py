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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        return self.recurse(root, targetSum)

    def stack(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if root is None:
            return []
        
        paths = []
        stack = [([root], targetSum)]

        while len(stack) > 0:
            nodes, remains = stack.pop()
            cur_node = nodes[-1]
            remains -= cur_node.val

            is_leaf_node = cur_node.left is None and cur_node.right is None
            if is_leaf_node:
                if remains == 0:
                    paths.append([n.val for n in nodes])
                continue

            if cur_node.left:
                stack.append((nodes + [cur_node.left], remains))
            
            if cur_node.right:
                stack.append((nodes + [cur_node.right], remains))
        
        return paths
            

    def recurse(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        def path_to_sum(n, prev_values: list[int]):
            if n is None:
                return None

            values = prev_values + [n.val]
            is_leaf_node = n.left is None and n.right is None
            if is_leaf_node:
                if targetSum == sum(values):
                    return [values]
                else:
                    return None
                
            left_path = path_to_sum(n.left, values)
            right_path = path_to_sum(n.right, values)

            if left_path is None and right_path is None:
                return None
            
            result = []
            if left_path is not None:
                result += left_path
            
            if right_path is not None:
                result += right_path
            
            return result
        

        result = path_to_sum(root, [])
        return result if result is not None else []


root = to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]); targetSum = 22
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().pathSum(root, targetSum))