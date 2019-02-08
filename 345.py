# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: 'str') -> 'str':
        vowels = "AEIOUaeiou"
        left, right = 0, len(s) - 1
        lst = list(s)
        while left < right:
            if lst[left] in vowels and lst[right] in vowels:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
            elif lst[left] in vowels and not lst[right] in vowels:
                right -= 1
            elif lst[right] in vowels and not lst[left] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(lst)