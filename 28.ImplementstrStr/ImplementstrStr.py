class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenNeedle = len(needle)
        lenHaystack = len(haystack)
        for index in range(lenHaystack-lenNeedle+1):
            if haystack[index:lenNeedle+index] == needle:
                return index
        return -1
        
