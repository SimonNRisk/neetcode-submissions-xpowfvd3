class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #given array of strings
        #group all anagrams into sublists
        #
        anamap = {}
        for string in strs:
            sorted_s = ''.join(sorted(string))
            if sorted_s not in anamap:
                anamap[sorted_s] = []
            anamap[sorted_s].append(string)
        return list(anamap.values())