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
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        pass

    def dfs_recurse(self, root: TreeNode) -> TreeNode:
        pass


    def dfs_stack(self, root: TreeNode) -> TreeNode:
        # find max depth
        # find leftmost deepest node
        # find rightmost deepest node
        # find least common ancestor of 2 nodes
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root

        stack = [(root, 1)]
        max_depth = 1

        l_leaf = None
        r_leaf = None

        # left first DFS
        while len(stack) > 0:
            node, depth = stack.pop()
            
            is_leaf = node.right is None and node.left is None
            if is_leaf:
                if max_depth < depth:
                    max_depth = depth
                    l_leaf = node
            
                continue
                        
            if node.right:
                stack.append((node.right, depth + 1))
            
            if node.left:
                stack.append((node.left, depth + 1))

        stack.append((root, 1))
        
        # right first DFS
        while len(stack) > 0:
            node, depth = stack.pop()
            
            is_leaf = node.right is None and node.left is None
            if is_leaf and max_depth == depth:
                r_leaf = node
                break

            if node.left:
                stack.append((node.left, depth + 1))
                        
            if node.right:
                stack.append((node.right, depth + 1))

        # find least common ancestor
        l_branch = l_leaf
        r_branch = r_leaf

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()

            is_leaf = node.left is None and node.right is None
            if is_leaf:
                continue

            if node.left is None or node.right is None:
                


        def find_lca(node):
            if node == l_leaf or node == r_leaf:
                return node
            
            # leaf node
            if node.left is None and node.right is None:
                return None
            
            # cannot be common ancestor
            if node.left is None or node.right is None:
                return find_lca(node.left if node.right is None else node.right)
            
            n_left = find_lca(node.left)
            n_right = find_lca(node.right)

            if n_left and n_right:
                return node
            
            return n_left if n_right is None else n_right

        lca = find_lca(root)

        return lca
    
    
    def dfs_stack2(self, root: TreeNode) -> TreeNode:
        # find max depth
        # find leftmost deepest node
        # find rightmost deepest node
        # find least common ancestor of 2 nodes
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root

        stack = [(root, 1)]
        max_depth = 1

        l_leaf = None
        r_leaf = None

        # left first DFS
        while len(stack) > 0:
            node, depth = stack.pop()
            
            is_leaf = node.right is None and node.left is None
            if is_leaf:
                if max_depth < depth:
                    max_depth = depth
                    l_leaf = node
            
                continue
                        
            if node.right:
                stack.append((node.right, depth + 1))
            
            if node.left:
                stack.append((node.left, depth + 1))

        stack.append((root, 1))
        
        # right first DFS
        while len(stack) > 0:
            node, depth = stack.pop()
            
            is_leaf = node.right is None and node.left is None
            if is_leaf and max_depth == depth:
                r_leaf = node
                break

            if node.left:
                stack.append((node.left, depth + 1))
                        
            if node.right:
                stack.append((node.right, depth + 1))

        # find least common ancestor
        l_branch = l_leaf
        r_branch = r_leaf

        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()

            is_leaf = node.left is None and node.right is None
            if is_leaf:
                continue

            if node.left is None or node.right is None:
                


        def find_lca(node):
            if node == l_leaf or node == r_leaf:
                return node
            
            # leaf node
            if node.left is None and node.right is None:
                return None
            
            # cannot be common ancestor
            if node.left is None or node.right is None:
                return find_lca(node.left if node.right is None else node.right)
            
            n_left = find_lca(node.left)
            n_right = find_lca(node.right)

            if n_left and n_right:
                return node
            
            return n_left if n_right is None else n_right

        lca = find_lca(root)

        return lca


root = to_tree([3,5,1,6,2,0,8,None,None,7,4])
root = to_tree([1])
root = to_tree([0,1,3,None,2])
#root = to_tree([1,2,2,3,3,None,None,4,4])
#root = to_tree([1,2,2,3,4,4,3])
#root = to_tree([1,2,2,None,3,None,3])
print(Solution().subtreeWithAllDeepest(root))