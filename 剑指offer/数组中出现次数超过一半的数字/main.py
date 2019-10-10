# -*- coding:utf-8 -*-


class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        tmp = {}
        length = len(numbers) / 2
        for i in numbers:
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1
            if tmp[i] > length:
                return i
        return -1
