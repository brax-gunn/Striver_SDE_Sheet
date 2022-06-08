class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tempSum = 0
        maxSum = float('-inf')
        
        for elem in nums:
            tempSum += elem
            maxSum = max(tempSum, maxSum)
            if tempSum < 0:
                tempSum = 0
        
        return maxSum