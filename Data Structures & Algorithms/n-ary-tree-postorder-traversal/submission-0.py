"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''
        n-ary tree - has list of children that are nodes
        post order traversal is L, R, M
        '''
        res = []
        def dfs(node):
            if not node:
                return
            '''
            if we have a node, check left, then right, then add
            '''
            for child in node.children:
                dfs(child)

            res.append(node.val)
            return
        dfs(root)
        return res