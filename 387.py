# 387. First Unique Character in a String

class Solution:
    
    def firstUniqChar(self, s: 'str') -> 'int':
        table = {}
        for i in range(len(s)):
            if not s[i] in table:
                table[s[i]] = i
            else:
                table[s[i]] = None
        
        for key in table:
            if table[key] is not None:
                return table[key]
        
        return -1
        