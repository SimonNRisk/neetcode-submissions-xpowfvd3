# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced?
        # left and right subtrees of each node differ by no more than 1
        
        '''
        balanced = True
        dfs(node):
            if not node:
                return 0 # no height
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            difference = abs(left_height - right_height)
            if difference > 1:
                balanced = False
            return 1 + max(left_height, right_height)

        '''
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            difference = abs(left_height - right_height)
            if difference > 1:
                balanced = False
            return 1 + max(left_height, right_height)
        dfs(root)
        return balanced