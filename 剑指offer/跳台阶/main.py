# -*- coding:utf-8 -*-


class Solution:

    def jumpFloor(self, number):
        a = 0
        b = 1
        while number:
            b = a + b
            a = b - a
            number -= 1
        return b
