# -*- coding:utf-8 -*-


class Solution:

    def rectCover(self, number):
        if number == 0:
            return 0
        a = 0
        b = 1
        while number:
            b = a + b
            a = b - a
            number -= 1
        return b
