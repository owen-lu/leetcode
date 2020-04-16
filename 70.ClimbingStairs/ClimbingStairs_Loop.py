class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        i = 3
        pre1 = 2
        pre2 = 1
        cur = 0
        while i <= n:
            cur = pre1 + pre2
            pre2 = pre1
            pre1 = cur
            i += 1
        return cur
