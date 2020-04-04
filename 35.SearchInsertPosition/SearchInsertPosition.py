class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums)-1)
 
    def binSearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        if end < start: return start      
        middle = int((start + end) / 2)
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            return self.binSearch(nums, target, middle+1, end)
        elif target < nums[middle]:
            return self.binSearch(nums, target, start, middle-1)
