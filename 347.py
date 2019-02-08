# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        
        freq_hash = dict()
        for n in nums:
            if n in freq_hash:
                freq_hash[n] += 1
            else:
                freq_hash[n] = 1
        heap = []
        import heapq
        
        for i in freq_hash.keys():
            heapq.heappush(heap, (freq_hash[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while len(heap) != 0:
            res.append(heapq.heappop(heap)[1])
        res.reverse()
        return res