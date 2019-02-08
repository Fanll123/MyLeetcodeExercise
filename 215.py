# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        import heapq
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
        return min_heap[0]