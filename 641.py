# 641. Design Circular Deque

class MyCircularDeque:
    
    class ListNode:
        def __init__(self, value):
            self.next = None
            self.val = value

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.__size = 0
        self.__cap = k
        self.__head, self.__tail = None, None
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            new_node = ListNode(value)
            new_node.next = self.__head
            self.__head = new_node
        else:
            self.__head = self.__tail = ListNode(value)
        self.__size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            self.__tail.next = ListNode(value)
            self.__tail = self.__tail.next
        else:
            self.__head = self.__tail = ListNode(value)
        self.__size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.__head = self.__head.next
            self.__size -= 1
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            if self.__size == 1:
                self.__head = self.__tail = None
            else:
                curr = self.__head
                for i in range(self.__size - 2):
                    curr = curr.next
                curr.next = None
                self.__tail = curr
            self.__size -= 1
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.__head.val

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.__tail.val

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.__size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.__size == self.__cap
