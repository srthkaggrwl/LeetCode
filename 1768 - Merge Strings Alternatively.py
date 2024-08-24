class Solution:
    def mergeAlternately(self, word1, word2):
        merge = []
        len1 = len(word1)
        len2 = len(word2)
        max_len = max(len1, len2)

        for i in range(max_len):
            if i < len1:
                merge.append(word1[i])
            if i < len2:
                merge.append(word2[i])
        return ''.join(merge)

# Example usage:
solution = Solution()
word1 = "abc"
word2 = "def"
print(solution.mergeAlternately(word1, word2))  # Output: "adbecf"
