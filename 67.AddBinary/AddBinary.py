class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        ptra = len(a) - 1
        ptrb = len(b) - 1
        result = ""
        overflow = False
        while ptra >= 0 and ptrb >= 0:
            if b[ptrb] == "0" and overflow == False:
                result = a[ptra] + result
            elif b[ptrb] == "0" and overflow == True:
                if a[ptra] == "0":
                    result = "1" + result
                    overflow = False
                else:
                    result = "0" + result
            elif b[ptrb] == "1" and overflow == False:
                if a[ptra] == "0":
                    result = "1" + result
                else:
                    result = "0" + result
                    overflow = True
            elif b[ptrb] == "1" and overflow == True:
                if a[ptra] == "0":
                    result = "0" + result
                else:
                    result = "1" + result
            ptra -= 1
            ptrb -= 1
        while ptra >= 0:
            if overflow == False:
                result = a[ptra] + result
                ptra -= 1
                continue
            if a[ptra] == "1":
                result = "0" + result
                ptra -= 1
            if a[ptra] == "0":
                result = "1" + result
                ptra -= 1
                overflow = False
        if overflow:
            result = "1"+ result
        return result
