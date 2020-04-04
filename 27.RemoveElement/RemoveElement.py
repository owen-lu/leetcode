class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_ = 0
        current = 0
        for _ in nums:
            if nums[current] != val:
                nums[len_] = nums[current]
                len_ = len_ + 1
            current = current + 1
        return len_
