# -*- coding:utf-8 -*-


class Solution:

    def Fibonacci(self, n):
        a = 0
        b = 1
        while n:
            b = b + a
            a = b - a
            n -= 1
        return a
