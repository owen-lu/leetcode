import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return x == 0
        mask = int(math.log10(x))
        middle = int(mask / 2)
        mask = 10 ** mask
        for index in range(0, middle+1):
            if int(x / mask) != int(x % 10):
                return False
            x = x % mask / 10
            mask = mask / 100
        return True
