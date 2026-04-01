class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longest_possible = len(strs[0])

        prefix = ""
        for i in range(longest_possible+1):
            prefix = strs[0][:i]
            print(prefix)
            for word in strs:
                if word[:i] != prefix:
                    print(f'returning {strs[0][:i-1]}')
                    return strs[0][:i-1]
        return strs[0]
            