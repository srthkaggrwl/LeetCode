class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        i = 0          
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
            if i == len(s):
                return True
        return False

    def numMatchingSubseq(self, s, words):
        j = 0  
        for word in words:
            if self.isSubsequence(word, s):
                j += 1
        return j

solution = Solution()
print(solution.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # Output should be 3
