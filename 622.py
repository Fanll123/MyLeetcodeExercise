# 622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k):
        self.__queue = []
        self.__cap = k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.__queue.append(value)
        return True
        

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            del self.__queue[0]
        return True
        
    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.__queue[0]
        
    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.__queue[len(self.__queue)-1]
        
    def isEmpty(self):
        return len(self.__queue) == 0
        
    def isFull(self):
        return len(self.__queue) == self.__cap
