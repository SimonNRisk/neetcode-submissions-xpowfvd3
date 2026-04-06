# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    # recursive solution:
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left), dfs(root.right))
        
        # return dfs(root)
    # iterative BFS solution
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            level +=1
        return level

