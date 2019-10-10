# -*- coding:utf-8 -*-


class Solution:

    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0:
            return -1
        res = range(n)
        index = m - 1
        while len(res) > 1:
            if index >= len(res):
                index %= len(res)
            res.pop(index)
            index += (m - 1)
        return res[0]
