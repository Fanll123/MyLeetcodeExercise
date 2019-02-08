# 38. Count and Say

class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        if n == 1:
            return "1"
        return self.count(self.countAndSay(n-1))
        
    def count(self, s: 'str') -> 'str':
        res = ""
        temp = s[0]
        i = 0
        cnt = 0
        for i in s:
            
            if i == temp:
                cnt += 1
            else:
                res = res + str(cnt) + temp
                temp = i
                cnt = 1   
                
        res = res + str(cnt) + temp
        
        return ''.join(res)