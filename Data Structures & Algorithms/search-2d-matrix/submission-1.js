class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const rows = matrix.length
        const cols = matrix[0].length
        let top = 0
        let bot = rows-1
        let row = Math.floor((top+bot)/2)
        while (top <= bot) {
            row = Math.floor((top+bot)/2)
            if (target > matrix[row][cols-1]) {
                top = row +1
            }
            else if (target < matrix[row][0]) {
                bot = row -1
            }
            //we've found the right row
            else {
                break
            }
        }
        if (top > bot) return false
        let left = 0
        let right = cols -1
        while (left <= right) {
            const mid = Math.floor((left + right)/2)
            if (matrix[row][mid] > target) {
                right = mid-1
            }
            else if (matrix[row][mid] < target) {
                left = mid+1
            }
            else {
                return true
            }
        }
        return false
    }
}
