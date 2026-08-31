class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[] for _ in range(numCourses)]
        for index, prereq in enumerate(prerequisites):
            prereqs[prerequisites[index][0]].append(prerequisites[index][1])

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        # We want to see, per course, is it possible to take without loop
        # Loop over courses, call DFS on the course
        def dfs(node):
            # Get a course number
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False
            
            states[node] = VISITING
            
            # No loop and not already visited
            for nei in prereqs[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        