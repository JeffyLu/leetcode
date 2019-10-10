# -*- coding:utf-8 -*-


class Solution:

    def NumberOf1(self, n):
        cnt = 0
        if n < 0:
            n += 2 ** 32
        while n > 0:
            if n % 2 == 1:
                cnt += 1
            n = n // 2
        return cnt
