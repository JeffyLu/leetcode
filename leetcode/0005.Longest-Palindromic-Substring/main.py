class Solution:

    def longestPalindrome(self, s):
        if not s:
            return None
        max_length = 1
        max_left = 0
        max_right = 0
        left = 0
        right = len(s) - 1
        while left < right:
            for i in range(right, left, -1):
                if s[i] != s[left]:
                    continue
                length = i - left + 1
                if length <= max_length:
                    break
                l = left
                r = i
                is_res = True
                while l < r:
                    if s[l] != s[r]:
                        is_res = False
                        break
                    l += 1
                    r -= 1
                if is_res:
                    max_left = left
                    max_right = i
                    max_length = length
                    break
            left += 1
        return s[max_left: max_right+1]
