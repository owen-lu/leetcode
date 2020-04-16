class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        if index < 0:
            return digits
        digits[index] += 1
        while index >= 0:
            if digits[index] != 10:
                break
            digits[index] = 0
            ptr = index - 1
            if ptr >= 0:
                digits[ptr] += 1
            else:
                digits.insert(0, 1)
            index -= 1
        return digits
