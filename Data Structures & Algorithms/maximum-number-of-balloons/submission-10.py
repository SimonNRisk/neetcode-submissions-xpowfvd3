class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #id think we want to build a freq map
        # from there can loop through, subtracting balloon letters
        # once cant subtract, return current count?
        self.freq_map = {}
        self.num_instances = 0
        for char in text:
            self.freq_map[char] = self.freq_map.get(char, 0) + 1
        
        #rather than looping to subtract, think about what the goal ois
        # to see the limiting factor - this is just the min:
        return min(self.freq_map.get("b", 0), self.freq_map.get("a", 0), self.freq_map.get("l", 0)//2, self.freq_map.get("o", 0)//2, self.freq_map.get("n", 0))