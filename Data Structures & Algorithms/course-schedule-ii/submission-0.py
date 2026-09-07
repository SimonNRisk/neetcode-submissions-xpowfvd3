from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq[i] = [a, b] means must take b before a (b->a)
        # If we have a loop we cant have a valid schedule
        # Thus we need a DAG
        # return a valid ordering to finish all courses
        # can return any



        # What this is essentially asking us:
        # Return a valid topological ordering of this DAG
        # Given this, we can use kahn's
        # essentially:
        '''
        Build two things as part of preprocessing:
            1. Adjacency list. adj[x] = list(the things that depend on x)
            - we need this so that we can, after processing x, look at what can now be processed
            2. Incoming degrees. indegree[x] = the number of things x depends on
            - we need this so we can know when we can start processing x
        After that we will use Kahns:
        - add things with indegree 0 to a queue (dont have any prereqs)
        - pop them one by one
        - decrement the indegree of the things in their adjacency list
        - if the indegree of those things is now 0, add them tot he queue, repeat
        '''
        # Courses are ordering 0 to numCourses -1
        indegree = {i: 0 for i in range(numCourses)}
        adj = defaultdict(list)
        # [0, 1] means to do 0, must do 1 (1->0)
        for course, prereq in prerequisites:
            indegree[course] +=1
            adj[prereq].append(course)
        # Nice!
        q = deque()
        for course, incoming_degrees in indegree.items():
            if incoming_degrees == 0:
                q.append(course)
        valid_ordering = []
        while q:
            processing = q.popleft()
            valid_ordering.append(processing)
            # Now mark as processed
            for dependent in adj[processing]:
                indegree[dependent] -=1
                if indegree[dependent] == 0:
                    q.append(dependent)
        if len(valid_ordering) == numCourses:
            return valid_ordering
        return []
