class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.helper(n, cache)

    def helper(self, n: int, cache: dict) -> int:
        if n == 1 or n == 2:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self.helper(n-1, cache) + self.helper(n-2, cache)
        return cache[n]
