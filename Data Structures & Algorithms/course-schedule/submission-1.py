from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # want to see if there is a possible valid topological ordering
        



        '''
        can use kahns
        calculate indegree, adj
        use to bfs with q and traverse graph
        '''
        adj = defaultdict(list)
        indegree = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] = indegree.get(course, 0) +1
        print(adj)
        print(indegree)
        q = deque()
        for course, incoming_degrees in indegree.items():
            if incoming_degrees == 0:
                q.append(course)
        if not q:
            return False #nothing with indegree (nowhere to start)
        
        # Now that we have q we can start
        processed = 0
        while q:
            processing = q.popleft()
            processed +=1
            # What do we do to it? we see what depends on it, and decrement their indegree. if 0 add to queue
            for dependant in adj[processing]:
                indegree[dependant] -=1
                if indegree[dependant] == 0:
                    q.append(dependant)
        return True if processed == numCourses else False









        '''
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
        '''
        