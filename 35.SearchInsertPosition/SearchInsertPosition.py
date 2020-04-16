class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums)-1)

    def binSearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if right < left: return left
        middle = int((left + right) / 2)
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            return self.binSearch(nums, target, middle+1, right)
        elif target < nums[middle]:
            return self.binSearch(nums, target, left, middle-1)
