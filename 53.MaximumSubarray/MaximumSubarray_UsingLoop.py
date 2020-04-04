class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        maxSum = curSum = 0
        for index in range(len(nums)):
            curSum = max(curSum + nums[index], nums[index])
            maxSum = curSum if index == 0 else max(maxSum, curSum)
        return maxSum
