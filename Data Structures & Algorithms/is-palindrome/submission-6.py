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
            print(f"comparing {s[left]} with {s[right]}")
            if not s[left].isalnum():
                print(f"moving left up because {s[left]} is not alnum")
                left +=1
            elif not s[right].isalnum():
                print(f"moving right up because {s[right]} is not alnum")
                right -=1
            elif not s[left].lower() == s[right].lower():
                print(f"not the same lowered: {s[left]}, {s[right]}")
                return False
            else:
                print(f"confirmed that {s[left]} and {s[right]} are equal")
                left+=1
                right -=1
        return True