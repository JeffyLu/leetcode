# -*- coding:utf-8 -*-


class Solution:

    def Power(self, base, exponent):
        n = abs(exponent)
        if n == 0:
            return 1

        res = self.Power(base, n >> 1)
        res *= res
        if n % 2 == 1:
            res *= base
        if exponent < 0:
            return 1 / res
        return res
