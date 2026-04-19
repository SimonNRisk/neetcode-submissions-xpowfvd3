# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        # Diameter = height of two subtrees
        # we need to iterate DFs
        # for every subtree
        # 1) height of left
        # 2) height of right
        # see if larger tahn current tracker of diameter
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(left+right, self.diameter)
            return 1+max(left, right)
        dfs(root)
        return self.diameter

        