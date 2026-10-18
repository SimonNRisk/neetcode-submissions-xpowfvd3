class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        backtracking:
        at each point can either do ( or )
        need a way to see if a state is valid:
            - n things used
            - can enforce the other one by only placing closing when have an opening down
        '''
        res = []
        running_res = []
        def backtrack(num_open, num_closed):
            nonlocal res
            nonlocal running_res
            nonlocal n
            if num_open == n and num_closed == n:
                res.append("".join(running_res))
                return
            if num_open < n:
                running_res.append("(")
                backtrack(num_open+1, num_closed)
                running_res.pop()
            if num_closed < num_open:
                running_res.append(")")
                backtrack(num_open, num_closed+1)
                running_res.pop()
            return
        backtrack(0, 0)

        return res


