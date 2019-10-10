# -*- coding:utf-8 -*-


class Solution:

    def FindContinuousSequence(self, tsum):
        results = []
        res = []
        sum_ = 0
        for i in xrange(1, tsum//2+2):
            res.append(i)
            sum_ += i
            while sum_ > tsum:
                sum_ -= res.pop(0)
            if sum_ == tsum and len(res) > 1:
                results.append(res[:])
                sum_ -= res.pop(0)
        return results
