class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x == 0:
            return 0
        if x < 0:
            negative = True
            x = abs(x)

        digits = floor(math.log10(x))
        mid = floor(digits / 2)
        mask  = 10 ** digits
        output = 0
        for index in range(0, mid+1):
            if index != digits-index:
                output += int(x / mask) * (10**index)
                output += int(x % 10) * (10**(digits-index))
            else:
                output += x * (10**index)
            x = int(x % mask / 10)
            mask = int(mask / 100)

        if negative:
            output = -output
        if output > 2**31-1 or output < -2**31:
            output = 0
        return output
        
