# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        
        while left < right:
            mid = (left+right)//2
            Badversion_result = isBadVersion(mid)
            if Badversion_result:
                right = mid
            else:
                left = mid + 1
        if isBadVersion(left):
            return left
        else:
            return right