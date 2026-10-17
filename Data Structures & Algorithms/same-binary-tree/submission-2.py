# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check that each node is the same
        # p, q are root nodes
        # can do dfs at root
        '''
        if nonequal, return False
        if one is present and the other isnt, return False
        if neither is present return True
        else (if equal):
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        '''
        def dfs(p, q):
            if p and not q:
                return False
            if q and not p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            return (dfs(p.left, q.left) and dfs(p.right, q.right))
        return dfs(p, q)
        