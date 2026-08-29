"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # First, create a mapping from old node to new node
        # Then, iterate over the mapping
        # For each old node, iterate over its neighbours
        # Search in the map for that neighbour, finding its
        # newer replacement
        # Append a reference to that newer replacement in the 
        # Processing node's neighbors list
        old_to_new = {}
        seen = set()
        start = node
        # DFS with stack
        stack = [start]
        while stack:
            old = stack.pop()
            old_to_new[old] = Node(val=old.val)
            for nei in old.neighbors:
                if nei not in seen:
                    stack.append(nei)
                    seen.add(nei)
        for old_node, new_node in old_to_new.items():
            for nei in old_node.neighbors:
                new_nei = old_to_new[nei]
                new_node.neighbors.append(new_nei)
        return old_to_new[node]

        