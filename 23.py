# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        newhead = ListNode(None)
        curr = newhead
        import heapq
        heap = []
        for i in range(len(lists)):
            root = lists[i]
            if root:
                heapq.heappush(heap, (root.val, i))
                lists[i] = lists[i].next
                
        
        while heap:
            # Pop the smallest value from the heap
            popped_val, idx = heapq.heappop(heap)
            
            curr.next = ListNode(popped_val)
            curr = curr.next
            
            root = lists[idx]
            if root:
                heapq.heappush(heap, (root.val, idx))
                lists[idx] = lists[idx].next
        
        return newhead.next