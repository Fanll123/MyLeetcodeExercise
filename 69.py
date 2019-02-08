# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left < right - 1:
            mid = (left + right) //2
            if mid**2 > x:
                right = mid
            elif (mid**2)< x:
                left = mid
            else:
                return mid
            
        if right**2 <= x:
            return right
        else:
            return left
            