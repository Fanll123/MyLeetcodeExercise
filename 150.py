# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import operator as ops
        operands = []
        opes = {'+': ops.add, 
                '-': ops.sub,
                '*':ops.mul,
                '/':ops.floordiv}
        
        for term in tokens:
            if term in opes:
                right, left = operands.pop(), operands.pop()
                res = opes[term](left,right)
                if term == '/':
                    if res < 0:
                        res = -(-left//right)
                operands.append(res)
            else:
                operands.append(int(term))
        return operands[0]
        