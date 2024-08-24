class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True

        i = 0
        
        for ch in t:
            if ch == s[i]:
                i += 1
            if i == len(s):
                return True

        return False

solution = Solution()
print(solution.isSubsequence("a","abcde"))