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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.stack_bfs(p, q)
        pass

    def recurse(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        return self.recurse(p.left, q.left) and self.recurse(p.right, q.right)

    def stack_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [(p, q)]

        while len(s)>0:
            n1, n2 = s.pop()
            if n1 is None and n2 is None:
                continue

            if n1 is None or n2 is None:
                return False
            
            if n1.val != n2.val:
                return False
            
            s.append((n1.left, n2.left))
            s.append((n1.right, n2.right))

        return True

    def stack_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur_layer = [(p, q)]
        next_layer = []

        while len(cur_layer) > 0:
            for n1, n2 in cur_layer:
                if n1 is None and n2 is None:
                    continue

                if n1 is None or n2 is None:
                    return False
                
                if n1.val != n2.val:
                    return False
                
                next_layer.append((n1.left, n2.left))
                next_layer.append((n1.right, n2.right))
            
            cur_layer = next_layer
            next_layer = []
        
        return True


p = to_tree([1,2,3]); q = to_tree([1,2,3])
p = to_tree([1,2]); q = to_tree([1,None,3])
#root = to_tree([3,9,20])
#root = to_tree([1,2,3]); targetSum = 5
#l = to_ll([1,2,3]); left = 1; right = 3
#l = to_ll([5]); left = 1; right = 1
#l = to_ll([5])
#l = to_ll([])

print(Solution().isSameTree(p, q))

# As we need to remove all nodes with duplicate value, resulting list may be empty, so add fake node at start
# We will need to have pointer to prev node to update ref, current node and next to compare values
# If cur.value = next.value then remove all nodes with that value
# else - advance 3 pointers