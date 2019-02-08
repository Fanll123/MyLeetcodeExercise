# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        fakehead = ListNode(None)
        fakehead.next = head
        curr, prev = head, fakehead
        duplicated = None
        
        while curr:
            if curr and curr.next and curr.val == curr.next.val:
                duplicated = curr.val

            if duplicated is None or duplicated != curr.val:
                prev.next = curr
                prev = curr

            curr = curr.next
        prev.next = None
        return fakehead.next