# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            if same_tree(node, subRoot):
                return True
            return (dfs(node.left) or dfs(node.right))
        def same_tree(node1, node2):
            if node1 and not node2:
                return False
            if not node1 and node2:
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            return (same_tree(node1.left, node2.left) and (same_tree(node1.right, node2.right)))
        return dfs(root)
        