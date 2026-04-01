class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const seen = new Set()
        let longest = 0
        let left = 0
        let right = 0
        while ((right <= s.length -1) && (left <= right)) {
            while (seen.has(s[right])) {
                seen.delete(s[left])
                left +=1
            }
            seen.add(s[right])
            longest = Math.max(longest, right-left+1)
            right +=1
        }
        return longest
    }
}