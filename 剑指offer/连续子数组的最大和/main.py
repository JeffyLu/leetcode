# -*- coding:utf-8 -*-


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        max_sum = max(array)
        for i in xrange(len(array)):
            tmp = array[i]
            for j in xrange(i+1, len(array)):
                tmp += array[j]
                if tmp > max_sum:
                    max_sum = tmp
        return max_sum
