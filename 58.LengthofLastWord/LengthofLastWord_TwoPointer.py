class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr1 = len(s) - 1
        ptr2 = 0
        while ptr1 >= 0:
            if s[ptr1] == " ":
                ptr1 -= 1
            else:
                break
        ptr2 = ptr1 - 1
        while ptr2 >=0:
            if s[ptr2] != " ":
                ptr2 -= 1
            else:
                break
        if ptr1 < 0:
            return 0
        else:
            return ptr1 - ptr2
