class Solution:

    def reverse(self, x):
        strx = str(x)
        if x < 0:
            res = int('-' + strx[1:][::-1])
        else:
            res = int(strx[::-1])
        return 0 if res < -2147483648 or res > 2147483647 else res
