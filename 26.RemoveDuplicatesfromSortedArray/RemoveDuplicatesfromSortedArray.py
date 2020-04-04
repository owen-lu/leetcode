class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        xLen = len(nums)
        if xLen <= 1: return xLen
        len_ = 1
        current = 0
        for _ in range(xLen-1):
            if nums[current] != nums[current+1]:
                nums[len_] = nums[current+1]
                len_ = len_ + 1
            current = current + 1
        return len_
