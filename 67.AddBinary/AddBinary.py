class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        ptra = len(a) - 1
        ptrb = len(b) - 1
        result = ""
        sum_ = ""
        preOverflow = False
        while ptra >= 0 and ptrb >= 0:
            currentOverflow = False
            if b[ptrb] == "0" and a[ptra] == "0":
                sum_ = "0"
            elif b[ptrb] == "0" and a[ptra] == "1":
                sum_ = "1"
            elif b[ptrb] == "1" and a[ptra] == "0":
                sum_ = "1"
            elif b[ptrb] == "1" and a[ptra] == "1":
                sum_ = "0"
                currentOverflow = True
            if preOverflow :
                if sum_ == "0":
                    sum_ = "1"
                else:
                    sum_ = "0"
                    currentOverflow = True
            preOverflow = currentOverflow
            result = sum_ + result
            ptra -= 1
            ptrb -= 1
        while ptra >= 0 :
            if preOverflow:
                if a[ptra] == "0":
                    result = "1" + result
                    preOverflow = False
                else:
                    result = "0" + result
            else:
                result = a[ptra] + result
            ptra -= 1
        if preOverflow:
            result = "1" + result
        return result
      
