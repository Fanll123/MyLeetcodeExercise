# 33. Search in Rotated Sorted Array

class Solution(object):
    def search(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(array) == 0:
            return -1
        left, right = 0, len(array)-1
        while left < right-1:
            mid = (left+right)//2
            if target == array[mid]:
                return mid
            if array[mid] >= array[left]:
                if target < array[mid] and target >= array[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif array[mid] < array[left]:
                if target > array[mid] and target <= array[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if array[left] == target:
            return left
        if array[right] == target:
            return right
        return -1