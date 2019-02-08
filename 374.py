# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left, right = 1, n
        
        while left <= right:
            mid = (left+right)//2
            guess_result = guess(mid)
            
            if guess_result < 0:
                right = mid - 1
            elif guess_result > 0:
                left = mid + 1
            else:
                return mid
            
        