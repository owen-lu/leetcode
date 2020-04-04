class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = self.countAndSay(n-1)
        len_ = len(s)
        stack = ""
        tmp = ""
        for current in range(len_):
            stack = stack + s[current]          
            if len_ == (current+1) or s[current] != s[current+1]:
                tmp = tmp + str(len(stack)) + s[current]
                stack = ""
        return tmp
