# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def search(node):
            print(node.val)
            if not node:
                return
            lca[0] = node
            if p.val > node.val and q.val > node.val:
                node = node.right
                search(node)
            elif p.val < node.val and q.val < node.val:
                node = node.left
                search(node)
            else:
                return
        
        search(root)
        return lca[0]
        