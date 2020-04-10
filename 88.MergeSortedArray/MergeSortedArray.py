class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # nums1
        j = n - 1  # nums2
        index = len(nums1)
        while i>=0 or j>=0:
            index -= 1
            if i<0: 
                nums1[index] = nums2[j]
                j -= 1
                continue
            if j<0:
                nums1[index] = nums1[i]
                i -= 1
                continue
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
                