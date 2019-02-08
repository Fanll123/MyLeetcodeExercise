# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: 'ListNode', val: 'int') -> 'ListNode':
        fakehead = ListNode(None)
        fakehead.next = head
        curr = fakehead
        while curr and curr.next:
            if curr.next.val == val:
                curr.next =curr.next.next
            else:
                curr = curr.next
        return fakehead.next
                
            