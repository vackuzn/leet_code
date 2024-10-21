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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        pass

    def recurse(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        # target_node -> get k distance nodes
        # get path from root to target_node
        # foreach parent node: get k - n nested nodes, exclude nodes in path, where n is distance from parent node to target

        stack = [(root, [root])]
        while len(stack) > 0:
            node, path = stack.pop()
            stack.append(node)

            if node.left == target:


                pass

        
        pass


root = to_tree([3,5,1,6,2,0,8,None,None,7,4])
#root = to_tree([1])
#root = to_tree([0,1,3,None,2])
#root = to_tree([1,2,2,3,3,None,None,4,4])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().dfs_stack(root) == Solution().dfs_stack2(root))
