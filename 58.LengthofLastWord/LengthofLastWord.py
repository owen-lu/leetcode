class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for x in s[::-1]:
            if x != ' ':
                counter += 1
            else:
                if counter == 0:
                    continue
                else:
                    break
        return counter
