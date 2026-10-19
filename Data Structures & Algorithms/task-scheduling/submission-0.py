class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        given array of CPU tasks
        tasks[i] is uppercase english char from A to Z
        given int n

        each CPU cycle allows completion of task

        identical tasks must be separated by n cycles
        min # of cycles to complete all tasks?

        add to the heap a tuple that starts with the index of when itll be done


        q and heap

        heap will have negative counts (max heap)
        q will have tasks: tuples of (-count, timewhendone)

        we will loop through while heap or q:
            if heap, pop from it
                add the cnt + 1 to the q, and add n to the curr time for "when this can be done"
            if q, popleft
                incremeent time
                if cnt non zero
        '''
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = deque()

        while max_heap or q:
            time+=1
            if max_heap:
                # process the thing on the heap
                el = heapq.heappop(max_heap) +1
                if el:
                    q.append((el, time+n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time


                
