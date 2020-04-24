class Solution:
    def changeBase(self, numAsString, b1, b2):
        numStart = ord("0")
        numEnd = ord("9")
        alCapitalStart = ord("A")
        alCapitalEnd = ord("Z")
        alStart = ord("a")
        alEnd = ord("z")
        sumBase10 = 0
        index = 0
        for c in numAsString[::-1]:
            asciiVal = ord(c)
            if numStart <= asciiVal <= numEnd:
                num = asciiVal - numStart
            elif alCapitalStart <= asciiVal <= alCapitalEnd:
                num = asciiVal - alCapitalStart + 10
            elif alStart <= asciiVal <= alEnd:
                num = asciiVal - alStart + 10
            sumBase10 = sumBase10 + num * (b1**index)
            index += 1
        output = ""
        while sumBase10 != 0:
            pop = int(sumBase10 % b2)
            c = ""
            if pop >= 10:
                c = chr(alCapitalStart + pop - 10)
            else:
                c = str(pop)
            output = c + output
            sumBase10 = int(sumBase10 / b2)
        return output
