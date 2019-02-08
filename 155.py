# 155. Min Stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__min = []
        self.__stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__stack.append(x)
        if len(self.__min) == 0 or x <= self.getMin():
            self.__min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.__stack[-1] == self.getMin():
            self.__min.pop()
        self.__stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.__stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__min[-1]
