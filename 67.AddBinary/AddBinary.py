class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ptra = len(a) - 1
        ptrb = len(b) - 1
        c = 0
        s = ""
        while ptra >= 0 or ptrb >= 0 or c == 1:
            if ptra >= 0:
                c = c + int(a[ptra])
                ptra = ptra - 1
            if ptrb >= 0:
                c = c + int(b[ptrb])
                ptrb = ptrb - 1
            s = str(c % 2) + s
            c = int(c / 2)
        return s
      
