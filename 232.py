# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue1 = []
        self.__queue2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.__queue1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.__queue2) == 0:
            for i in range(len(self.__queue1)):
                self.__queue2.append(self.__queue1[-1])
                self.__queue1.pop()
        res = self.__queue2[-1]
        self.__queue2.pop()
        return res

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None
        elif len(self.__queue1) > 0:
            return self.__queue1[0]
        else:
            return self.__queue2[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (len(self.__queue1) == 0 and len(self.__queue2) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()