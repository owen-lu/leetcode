class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
        length = len(s)
        for index in range(length - 1):     
          if map[s[index+1]] > map[s[index]]:
            counter = counter - map[s[index]]
          else:
            counter = counter + map[s[index]]
        return counter + map[s[length - 1]]
