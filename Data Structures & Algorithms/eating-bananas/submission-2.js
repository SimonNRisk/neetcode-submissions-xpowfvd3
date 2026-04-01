class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let left = 1
        let right = 0
        for (const pile of piles) {
            right = Math.max(right, pile)
        }
        let result = right
        while (left <= right) {
            const rate = Math.floor((right+left)/2)
            let hours = 0
            for (const pile of piles) {
                hours += Math.ceil(pile/rate)
            }
            if (hours <= h) {
                result = Math.min(rate, result)
                right = rate -1
            }
            else {
                left = rate + 1
            }
        }
        return result
    }
}
