# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def dfs(node):
#             if not node:
#                 return
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)
#         dfs(root)
#         return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #use a stack
        res = []
        stack, cur = [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            popped = stack.pop()
            res.append(popped.val)
            cur = popped.right
        return res
        




        