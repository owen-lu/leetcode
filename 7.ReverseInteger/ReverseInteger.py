class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        recv = 0
        while x != 0:
            pop = int(x % 10)
            recv = recv * 10 + pop
            x = int(x / 10)
        if negative:
            recv = -recv
        if recv > 2**31-1 or recv < -2**31:
            return 0
        return recv
        
