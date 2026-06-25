class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {}
        outgoing = {}
        for truster, trustee in trust:
            outgoing[truster] = outgoing.get(truster, [])
            outgoing[truster].append(trustee)
            incoming[trustee] = incoming.get(trustee, [])
            incoming[trustee].append(truster)
        
        trusted_candidates = []
        for i in range(1, n+1):
            num_trustees = len(incoming.get(i, []))
            if num_trustees == n-1:
                trusted_candidates.append(i)
        
        print(trusted_candidates)
        
        for candidate in trusted_candidates:
            if outgoing.get(candidate, 0) == 0:
                return candidate
        
        return -1
        