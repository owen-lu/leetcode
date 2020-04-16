class Solution:
    def mySqrt(self, x: int) -> int:
        t = int(x / 2)
        while (t * t) > x:
            t = int(t / 2)
        while (t * t) <= x:
            t = t + 1
        return t - 1
