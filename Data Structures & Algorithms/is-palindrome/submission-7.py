class Solution:
    def isPalindrome(self, s: str) -> bool:
        #case insensitive
        #ignores non alphanumeric
        #could reverse, but thats O(n)
        #can we do better?
        #even though its both O(n), one has early exit, one mandates O(2n)
        #Two pointer is O(2), reverse id new array to compare (O(n))
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left +=1
            elif not s[right].isalnum():
                right -=1
            elif not s[left].lower() == s[right].lower():
                return False
            else:
                left+=1
                right -=1
        return True