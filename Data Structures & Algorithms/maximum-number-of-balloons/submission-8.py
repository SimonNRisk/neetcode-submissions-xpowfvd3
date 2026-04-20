class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #id think we want to build a freq map
        # from there can loop through, subtracting balloon letters
        # once cant subtract, return current count?
        self.freq_map = {}
        self.num_instances = 0
        for char in text:
            self.freq_map[char] = self.freq_map.get(char, 0) + 1
        
        print(self.freq_map.items())
        # now we have a freq map
        self.balloon_letter_cost = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1
        }
        
        while True:
            try:
                self._remove_balloon_instance()
                self.num_instances +=1
            except:
                break
        return self.num_instances


    def _remove_balloon_instance(self):
        for char, cost in self.balloon_letter_cost.items():
            if self.freq_map.get(char, 0) < cost:
                raise ValueError
            self.freq_map[char] -= cost        

        