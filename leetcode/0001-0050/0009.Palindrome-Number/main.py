class Solution:

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x < 10:
            return True
        res = 0
        while res < x:
            res = res * 10 + x % 10
            x = x // 10
        return True if x == res or x == res // 10 else False
