class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)  # Convert string to list
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        
        return ''.join(s)  # Join list back into a string

