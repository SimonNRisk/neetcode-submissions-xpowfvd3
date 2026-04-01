class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        const count = new Map()
        let result = 0
        let left = 0
        for (let right = 0; right < s.length; right++) {
            count.set(s[right], (count.get(s[right]) ?? 0) +1)

            //now if invalid window
            while ((right - left + 1) - (Math.max(...count.values())) > k) {
                count.set(s[left], count.get(s[left]) -1)
                left+=1
            }
            //now that its valid
            result = Math.max(result, right-left+1)
        }
        return result
    }
}
