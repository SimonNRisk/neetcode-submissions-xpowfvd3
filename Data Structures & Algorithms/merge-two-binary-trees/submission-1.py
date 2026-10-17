# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        get two roots
        when nodes are both present, sum them
        if only one is present, use it
        if neither present, node
        from our dfs we want to return the merged tree
        take base examples:
        1) if root1 and not root2: return root1
            root1.left = dfs(root1.l)
        2) if not root1 and root2: return root2
        3) if not root1 and not root2: return None
        4) if root1 and root2: root1.val += root2.val. return root1

        but what about if q has kids and p doesnt?
        def dfs(p, q):
            if not p and q:
                p = TreeNode(val=q.val)
            if p and not q:
                pass
            if not p and not q:
                return None
            if p and q:
                p.val = p.val + q.val



        '''
        def dfs(p, q):
            if p and not q:
                return p
            if not p and q:
                p = q # maybe we need a deep copy?
                return p
            if not p and not q:
                return None
            # Else
            p.val += q.val
            p.left = dfs(p.left, q.left)
            p.right = dfs(p.right, q.right)
            return p
        merged_tree = dfs(root1, root2)
        return merged_tree



