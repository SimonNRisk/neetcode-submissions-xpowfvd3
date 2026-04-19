# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced = True
        # all need to be balanced
        # we can do dfs, start bottom up?
        # return height?
        def dfs(node):
            if not node:
                return 0
            left_height = 1 + dfs(node.left)
            right_height = 1 + dfs(node.right)
            if abs(left_height - right_height) > 1:
                self.isbalanced = False
            return max(left_height, right_height)
        dfs(root)
        return self.isbalanced
        