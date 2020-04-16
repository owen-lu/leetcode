class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binSearch(x, 0, x)

    def binSearch(self, x: int, left: int, right: int) -> int:
        if right < left:
            return right
        middle = int((right + left) / 2)
        if middle**2 == x:
            return middle
        if middle**2 > x:
            return self.binSearch(x, left, middle-1)
        if middle**2 < x:
            return self.binSearch(x, middle+1, right)
