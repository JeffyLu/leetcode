class Solution:

    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        dup = {}
        for i in range(len(s)):
            if s[i] in dup:
                start = max(dup[s[i]]+1, start)
            dup[s[i]] = i
            max_length = max(i - start + 1, max_length)
        return max_length
