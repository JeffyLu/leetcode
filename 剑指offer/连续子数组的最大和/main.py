# -*- coding:utf-8 -*-


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        i = 0
        res = array[0]
        while i < len(array):
            tmp_res = 0
            j = i
            while j < len(array):
                tmp_res += array[j]
                if tmp_res > res:
                    res = tmp_res
                j += 1
                if tmp_res < 0:
                    i = j
                    break
            if j == len(array):
                break
        return res
