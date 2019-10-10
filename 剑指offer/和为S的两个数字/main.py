# -*- coding:utf-8 -*-


class Solution:

    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        dup = {}
        res = []
        for i in array:
            if i not in dup:
                dup[tsum-i] = i
            else:
                res.append((dup[i], i))
        return res and min(res, key=lambda x: x[0] * x[1])
