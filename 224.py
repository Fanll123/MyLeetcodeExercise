# 224. Basic Calculator

class Solution:

    def calculate(self, s: 'str') -> 'int':
        inBrac = []
        BracCount = 0
        res = 0
        left = []
        ops_sign = 1
        count , length = 0, len(s)
        for term in s:
            count += 1
            if term == '':
                continue
            if term == '(':
                if BracCount == 0:
                    BracCount += 1
                    continue
                else:
                    BracCount += 1
            if BracCount > 0:
                inBrac.append(term)
                if term == ')':
                    BracCount -= 1
                    if BracCount == 0:
                        inBrac.pop()
                        res += self.calculate(inBrac) * ops_sign
                        inBrac = []
                    else:
                        continue
            else:
                if term == '+':
                    if len(left)>0:   
                        res += ops_sign*(int(''.join(left)))
                        left = []
                    ops_sign = 1
                elif term == '-':
                    if len(left)>0: 
                        res += ops_sign*(int(''.join(left)))
                        left = []
                    ops_sign = -1
                elif term.isdigit():
                    left.append(term)
            if count == length:
                if len(left)>0:
                    res += ops_sign*(int(''.join(left)))
                    left = []
        return res
                    