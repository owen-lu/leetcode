class Solution:
    def reverseBits(self, n: int) -> int:
        index = 0
        output = 0
        while index <= 31:
            output = output << 1
            if n & 1 == 1:
                output = output | 1
            n = n >> 1
            if n == 0:
                output = output << (31 - index)
                break
            index = index + 1
        return output
