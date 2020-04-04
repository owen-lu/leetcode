class Solution:
    def isValid(self, s: str) -> bool:  
        map = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in map:
                if not stack or stack.pop(0) != map[c]:
                    return False
            else:
                stack.insert(0, c)
        return stack == []
