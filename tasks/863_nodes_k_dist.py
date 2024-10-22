from typing import Optional


# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, value: object) -> bool:
        return self.val == value.val

    def __repr__(self) -> str:
        return str(self.val)


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
        return self.recurse(root, target, k)

    def recurse(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        # target_node -> get k distance nodes
        # get path from root to target_node
        # foreach parent node: get k - n nested nodes, exclude nodes in path, where n is distance from parent node to target
        if root is None:
            return []
        
        if k == 0:
            return [target.val]
               
        def get_path_to_node(path):
            node = path[-1]
            if node == target:
                return path
            
            for n in (node.left, node.right):
                if n:
                    result = get_path_to_node(path + [n])
                    if result is not None:
                        return result

            return None
    
        path_to_node = get_path_to_node([root])
        
        def get_k_distance_children(node: TreeNode, exclusions: list[TreeNode], k: int) -> list[TreeNode]:
            if k == 0:
                return [node.val]
            
            result = []
            
            for n in (node.left, node.right):
                if n and n not in exclusions:
                    node_res = get_k_distance_children(n, exclusions, k - 1)
                    result += node_res
            
            return result
        
        result = []
        for i, node in enumerate(path_to_node[::-1]):
            if i > k:
                break

            result += get_k_distance_children(node, path_to_node, k-i)
        
        return result


root = to_tree([3,5,1,6,2,0,8,None,None,7,4]); target = TreeNode(5); k = 2
#root = to_tree([1])
#root = to_tree([0,1,3,None,2])
#root = to_tree([1,2,2,3,3,None,None,4,4])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().distanceK(root, target, k))
