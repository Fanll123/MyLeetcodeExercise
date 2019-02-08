# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        if len(s) <= 1:
            return True
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1

        return True
            