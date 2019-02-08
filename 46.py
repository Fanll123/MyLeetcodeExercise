# 46. Permutations

class Solution:
    def backTrack(self, ans, permutation, nums):
        if len(permutation) == len(nums):
            ans.append(permutation[:])
            return
        for num in nums:
            if num not in permutation:
                permutation.append(num)
                self.backTrack(ans, permutation, nums)
                permutation.pop()
        return
        
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        ans, permutation = [], []
        self.backTrack(ans, permutation, nums)
        return ans