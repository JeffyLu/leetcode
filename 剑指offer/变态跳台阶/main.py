# -*- coding:utf-8 -*-


class Solution:

    def jumpFloorII(self, number):
        if number <= 1:
            return number
        return 1 << number - 1
