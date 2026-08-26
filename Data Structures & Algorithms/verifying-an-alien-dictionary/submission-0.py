class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c : i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            #-1 because comparing pairs
            w1, w2 = words[i], words[i+1]
            # what to compare?
            # go through letters
            for j in range(len(w1)):
                # if prefix
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    # see order first
                    # false would be
                    if order_index[w2[j]] < order_index[w1[j]]:
                        return False
                    break
        return True

        