class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        # Correct!
        # now that we have our adjacency list....
        visited = set()
        result = 0
        for node in range(n):
            if node not in visited:
                # Do DFS
                # mark all as visited
                # go again
                result +=1
                stack = [node]
                while stack:
                    n = stack.pop()
                    for nei in adj_list[n]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
        return result