class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26

            # get letter freq key
            for char in word:
                alpha_index = ord(char) - ord('a')
                count[alpha_index] += 1
            
            key = tuple(count)

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return list(anagrams.values())


        '''
        anagrams = {}
        for word in strs: #O(n)
            sorted_word = "".join(sorted(word)) # O(2m logm)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values()) # O(n)
        '''
        
        # n = number of words in strs
        # m = length of word

        # can we make this better?
        # i think yes - letter frequency is a faster way to determine if anagrams rather than sorted order
        # 