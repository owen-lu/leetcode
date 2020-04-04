class Solution:   
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x < -2**31: return 0
        revert = None
        if x >= 0:
            revert = int(str(x)[::-1])
        else:
            revert = int("-" + str(x)[1:][::-1])
        if revert > 2**31-1 or revert < -2**31: return 0
        return revert
