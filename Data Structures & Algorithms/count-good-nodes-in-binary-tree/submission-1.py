# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        dfs(root, path_max)
        init pathmax at -inf

        save prev pathmax

        if val > pathmax
            good +=1
            pathmax = val
        '''
        init_pm = float('-inf')
        num_good = 0
        def dfs(node, path_max):
            nonlocal num_good
            if not node:
                return
            if node.val >= path_max:
                num_good +=1
                path_max = node.val
            
            dfs(node.left, path_max)
            dfs(node.right, path_max)
            return
        
        dfs(root, init_pm)
        return num_good
