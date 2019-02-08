# 707. Design Linked List

class MyLinkedList:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
        
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Head = None

    def search(self, index):
        # return the index-th node, if not, return None
        if self.Head is None or index < 0:
            return None
        curr = self.Head
        for i in range(index):
            curr = curr.next
            if not curr:
                return None
        return curr
        
    def get(self, index: 'int') -> 'int':
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.search(index)
        if node is None:
            return -1
        else:
            return node.val

    def addAtHead(self, val: 'int') -> 'None':
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        new_head.next = self.Head
        self.Head = new_head

    def addAtTail(self, val: 'int') -> 'None':
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.Head is None:
            self.Head = ListNode(val)
        else:
            curr = self.Head
            while curr.next is not None:
                curr = curr.next
            curr.next = ListNode(val)

    def addAtIndex(self, index: 'int', val: 'int') -> 'None':
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        if self.Head is None:
            return
        if index < 0:
            return
        prevnode = self.search(index - 1)
        if prevnode is None:
            return
        else:
            new_node = ListNode(val)
            new_node.next = prevnode.next
            prevnode.next = new_node
        return
        

    def deleteAtIndex(self, index: 'int') -> 'None':
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.Head = self.Head.next
            return
        if self.Head is None:
            return
        if index < 0:
            return
        prevnode = self.search(index - 1)
        if prevnode is None:
            return
        else:
            if prevnode.next is None:
                return
            else:
                prevnode.next = prevnode.next.next
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)