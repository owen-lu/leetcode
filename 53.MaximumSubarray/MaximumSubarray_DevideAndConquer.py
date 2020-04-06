class Solution: 
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums: List[int], start: int, end: int) -> int:
        if start > end: return None
        if start == end: return nums[start]
        middle = int((start + end) / 2)
     
        leftMax = self.helper(nums, start, middle-1)
        rightMax = self.helper(nums, middle+1, end)
        
        midSum = nums[middle]
        midMax = nums[middle]  
        for index in range(middle-1, start-1, -1):
            midSum = midSum + nums[index]
            midMax = max(midSum, midMax)
        midSum = midMax
        for index in range(middle+1, end+1):
            midSum = midSum + nums[index]
            midMax = max(midSum, midMax)
         
        resMax = max(leftMax, midMax) if leftMax is not None else midMax
        resMax = max(rightMax, resMax) if rightMax is not None else resMax
        return resMax