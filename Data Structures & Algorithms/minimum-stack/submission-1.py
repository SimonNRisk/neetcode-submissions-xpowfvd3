class MinStack:

    def __init__(self):
        self.stack = []
        self.min_el = float('inf')

    def push(self, val: int) -> None:
        self.stack.append((val, self.min_el))
        self.min_el = min(self.min_el, val)
        

    def pop(self) -> None:
        popped_val, popped_min = self.stack.pop()
        if popped_val < popped_min:
            self.min_el = popped_min
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_el
        
