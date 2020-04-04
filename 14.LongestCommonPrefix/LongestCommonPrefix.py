class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:     
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        common = ""
        first = strs.pop(0)
        for index in range(len(first)):
            pattern = first[0:index+1]
            for item in strs: 
                if pattern != item[0:index+1]:
                    return common
            common = pattern          
        return common
